from collections import namedtuple
from Veritas import get_data
from Veritas import tokenizer
from fairseq import data
from fairseq import utils
from fairseq import tasks
from fairseq.sequence_generator import SequenceGenerator
import numpy as np
import torch
from Veritas import args
from Veritas import generator_utils
from Veritas import nlpBackend


class ModelApi():
    def __init__(self) -> None:
        self.nlp = nlpBackend.BasicFunctions()
        self.chkpath = get_data("checkpoint_best.pt")
        #self.translator: SequenceGenerator = self.m.getTranslatorModel()
        # <- is for the outcommented code below
        self.Batch = namedtuple('Batch', 'srcs tokens lengths')
        self.Translation = namedtuple(
            'Translation', 'src_str hypos pos_scores alignments')  # <- this one as well
        self.print_alignment = False
        self.args = args.Args()
        self.args.buffer_size = 2  # not required for work

    def translate(self, text: str) -> list:
        """
        Takes text as an input and returns a sparql answer for each question given.
        Inputs:
            text: A text of questions (no need to remove question marks, points or lower the characters, we do that for you!)
        Outputs:
            A map containing the input split in sentences and the output as a json string
        """
        resultStorage = []
        sentences: list = self.nlp.extractSentences(text)
        sentences: list = [[str(i).lower().replace(
            "?", "").replace(".", "")] for i in sentences]
        # print(sentences)
        # generates results from text
        ret: list = self.generate(text=sentences)
        for entry in ret:
            editedEntry: str = entry[0]  # get's string from list
            # removes number and formating in front of sentence
            editedEntry: str = editedEntry.split("\t")[2]
            # print("*************")
            # print(entry)
            # print("*************")
            # should decode the AI generated translation to an actual one
            decodedSparql: str = generator_utils.decode(editedEntry)
            result: dict = generator_utils.query_dbpedia(decodedSparql)
            resultStorage.append(result)
        return resultStorage

    """
    Not needed
    def buffered_read(self, buffer_size):
            buffer = []
            for src_str in sys.stdin:  # get's string from intput
                # add string whithout white space in the beginning and end
                buffer.append(src_str.strip())
                # if the length of the buffer is larger then the buffer_size specified
                if len(buffer) >= buffer_size:
                    yield buffer  # return the buffer as generator
                    buffer = []  # empties buffer

            if len(buffer) > 0:  # if the final buffer is not empty yield its
                yield buffer
    """
    # generates batches, takes in the input lines (from the buffered_read function), arguments, task??, max_positions

    def make_batches(self, lines, args, task, max_positions):
        tokens = [
            tokenizer.Tokenizer.tokenize(
                src_str, task.source_dictionary, add_if_not_exist=False).long()
            for src_str in lines
        ]  # cretes tokens via tokenizer from src_str and ?encoding? dictionary
        #print(f"Tokens in make batches: {tokens}")
        # calculate the lenghts as np.array by returning the total number of elements in the array e.g. array of size (4,4)=4*4=16
        lengths = np.array([t.numel() for t in tokens])
        itr = task.get_batch_iterator(  # And here we are lost... creates a batch iterator
            dataset=data.LanguagePairDataset(
                tokens, lengths, task.source_dictionary),  # using a LanguagePairDataset
            # max amount of tokens (optional?)
            max_tokens=self.args.max_tokens,
            # max amount of sentences (optional?)
            max_sentences=self.args.max_sentences,
            # max number of positions?? (optional??)
            max_positions=max_positions,
        ).next_epoch_itr(shuffle=False)  # returns unshuffled batch
        for batch in itr:  # iterate through batches
            #print(f"Tokens after data.LanguagePairDataset: {batch['net_input']['src_tokens']}")
            yield self.Batch(  # return a batch using a generator
                # places the corresponding line to a batch id in a list?
                srcs=[lines[i] for i in batch['id']],
                # tokens are the src_tokens -> tokens of the input?
                tokens=batch['net_input']['src_tokens'],
                # get the lenghts of the src_inputs token vectors
                lengths=batch['net_input']['src_lengths'],
            ), batch['id']  # return bartch id

    def generate(self, text: list):
        """
        text: Takes in a list of sentences as input, don't call by ourself if you don't know what you are doing
        """
        resultStorage: list = []
        if self.args.buffer_size < 1:  # set's buffer size to a min of 1
            self.args.buffer_size = 1
        # if not number of max tokens and max_sentences is given -> set max_sentences to
        if self.args.max_tokens is None and self.args.max_sentences is None:
            self.args.max_sentences = 1

        assert not self.args.sampling or self.args.nbest == self.args.beam, \
            '--sampling requires --nbest to be equal to --beam'
        assert not self.args.max_sentences or self.args.max_sentences <= self.args.buffer_size, \
            '--max-sentences/--batch-size cannot be larger than --buffer-size'

        # print(args)# print arguments

        # checks if cuda can be used
        use_cuda = torch.cuda.is_available() and not self.args.cpu

        # Setup task, e.g., translation
        task = tasks.setup_task(self.args)  # idk??

        # Load ensemble
        print('| loading model(s) from {}'.format(
            self.args.path))  # useless info
        # model_paths = self.args.path.split(':')#useless
        model_paths = [self.chkpath]
        models, model_args = utils.load_ensemble_for_inference(model_paths, task, model_arg_overrides=eval(
            self.args.model_overrides))  # load models

        # Set dictionaries
        tgt_dict = task.target_dictionary

        # Optimize ensemble for generation
        for model in models:  # iterate through models
            model.make_generation_fast_(  # uses make generateion fast method
                # uses onliner to check if beamable_mm_beam_size is None or not
                beamable_mm_beam_size=None if self.args.no_beamable_mm else self.args.beam,
                need_attn=self.args.print_alignment,  # boolean if a print alignment is needed
            )
            if self.args.fp16:  # half the model????
                model.half()

        # Initialize generator
        translator = SequenceGenerator(
            tgt_dict, beam_size=self.args.beam, min_len=self.args.min_len,
             stop_early=(not self.args.no_early_stop),sampling=self.args.sampling,
            normalize_scores=(not self.args.unnormalized),
            len_penalty=self.args.lenpen, unk_penalty=self.args.unkpen,
             sampling_topk=self.args.sampling_topk, #can't be used in fairseq 0.6.2
            temperature=self.args.sampling_temperature,
            diverse_beam_strength=self.args.diverse_beam_strength,diverse_beam_groups=self.args.diverse_beam_groups,
        )

        if use_cuda:
            translator.cuda()  # if cuda can be used use it

        # Load alignment dictionary for unknown word replacement
        # (None if no unknown word replacement, empty if no path to align dictionary)
        align_dict = utils.load_align_dict(self.args.replace_unk)

        # Uses named tuple to init values for later and palce src sentence as src_strs
        def make_result(src_str, hypos):
            result = self.Translation(  # create a result Tupple (named tupple result)
                src_str='O\t{}'.format(src_str),
                hypos=[],
                pos_scores=[],
                alignments=[],
            )
            #print(f"Hypos at beginning of make_result: {hypos}")
            # Process top predictions
            # iterates through top predictions?
            for hypo in hypos[:min(len(hypos), self.args.nbest)]:
                hypo_tokens, hypo_str, alignment = utils.post_process_prediction(  # post processes the prediction
                    # pass tokens of current prediction and convert to int and then make it for cpu compatible?
                    hypo_tokens=hypo['tokens'].int().cpu(),
                    src_str=src_str,  # gives the input string
                    alignment=hypo['alignment'].int().cpu(
                    ) if hypo['alignment'] is not None else None,  # checks if alignmemt is needed
                    align_dict=align_dict,  # passes dict with words for alignment
                    # gives the target dictionary (decode one???)
                    tgt_dict=tgt_dict,
                    remove_bpe=self.args.remove_bpe,  # bool idk what for
                )
                # use the hypons list of the result to save formatted post_process_prediction score
                #print(f"Hypo tokens and string in make result after post process prediction:{hypo_tokens}, {hypo_str} ")
                result.hypos.append(
                    'H\t{}\t{}'.format(hypo['score'], hypo_str))
                result.pos_scores.append('P\t{}'.format(  # does the same for the positional score in list format
                    ' '.join(map(
                        lambda x: '{:.4f}'.format(x),
                        hypo['positional_scores'].tolist(),
                    ))
                ))
                result.alignments.append(  # saves the formatted stuff in the alignements section of the result, if print_alignment is not false
                    'A\t{}'.format(
                        ' '.join(map(lambda x: str(utils.item(x)), alignment)))
                    if self.args.print_alignment else None
                )
            return result  # returns result

        def process_batch(batch):  # takes in a batch
            """
            Processes the batch, don't call directly except you know what you are doing
            """
            tokens = batch.tokens  # sets tokens to batch tokens
            #print(f"Tokens in process batch: {tokens}")
            lengths = batch.lengths  # sets length to batch lenght

            if use_cuda:
                tokens = tokens.cuda()  # loads tokens on cuda
                lengths = lengths.cuda()  # loads lengths on cuda

            # prepare encoder input with tokens and and src_lengths
            encoder_input = {"net_input": {
                'src_tokens': tokens, 'src_lengths': lengths}}
            #print(f"\t Tokens: \t {tokens}")
            # Problem should appear around here!
            translations = translator.generate(  # generate actual translation from encoder input and maxlen
                models,
                encoder_input,
                maxlen=int(self.args.max_len_a * \
                           tokens.size(1) + self.args.max_len_b),
            )
            ####
            # print("----------------------")
            # return a list of results
            #print(f"\n > {translations}\n")
            # print("----------------------")
            return [make_result(batch.srcs[i], t) for i, t in enumerate(translations)]

        max_positions = utils.resolve_max_positions(  # resolves max positions
            task.max_positions(),  # how???
            *[model.max_positions() for model in models]
        )

        if self.args.buffer_size > 1:  # checks buffer size
            # prints current buffer size
            print('| Sentence buffer size:', self.args.buffer_size)
        #print('| Type the input sentence and press return:')
        for inputs in text:  # self.buffered_read(self.args.buffer_size):
            # stores indicies of batches (for later structering the answer?)
            # print(inputs)
            indices = []
            results = []  # stores results
            # takes user input and generates batch and corresponding ID for iteration
            for batch, batch_indices in self.make_batches(inputs, self.args, task, max_positions):
                # adds batch indecies to indicies list
                indices.extend(batch_indices)
                # results will be returned by process batch
                results += process_batch(batch)
            for i in np.argsort(indices):  # iterates through sorted arrays?
                # takes result corresponding to the input batch id
                result = results[i]
                #print(f"result: {result}")
                # print(result.src_str)  # print the input string (i.e. the question)
                resultStorage.append(result.hypos)  # stores result
                # print(result.hypos)
                # prints other stuff not needed for us
                # for hypo, pos_scores, align in zip(result.hypos, result.pos_scores, result.alignments):
                # print(hypo)
                # print(pos_scores)
                # if align is not None:
                #   print(align)
        return resultStorage


if __name__ == "__main__":  # DEBUG
    m = ModelApi()
    ret = m.translate(
        "What is the biggest mountin in the US? What is the capital of China?")
    print(ret)
