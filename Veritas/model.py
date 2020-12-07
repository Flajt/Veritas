from typing import Dict
from fairseq.sequence_generator import SequenceGenerator
from fairseq.models.fconv_self_att import FConvDecoder
from fairseq.models.fconv_self_att import FConvEncoder
from fairseq.data.dictionary import Dictionary
from fairseq.models.fconv_self_att import FConvModelSelfAtt
import torch
"""
Here is my first nearly working approach happening, this one can't predict yet, I tried to import all methods from the respective models they used, but I can't decoded them yet to get
it to work. In my (unqualified) opinion the problem is that you need to preprocess the data in a certain way to pass it into the model, but idk how.
The goal would be to have a wrapper were you can pass a sentence and it would return the Sparql translation of it for further use
"""


class Model():
    """Contains initialized Model from fairseq"""

    def __init__(self) -> None:
        # Creates dictionary, seems to be the wrapper for embedding layers I guess
        self.enDic = Dictionary()
        self.deDic = Dictionary()
        # loads the dictionary from the papers author
        self.enDic.add_from_file("./data/dict.en.txt")
        self.deDic.add_from_file("./data/dict.sparql.txt")
        # loads modelcheckpoint to cpu
        self.chkpath = "./data/checkpoint_best.pt"
        self.checkpoint = torch.load(
            self.chkpath, map_location=torch.device('cpu'))["model"]
        self.f = FConvModelSelfAtt(encoder=FConvEncoder(self.enDic),
                                   decoder=FConvDecoder(self.deDic, embed_dim=768, out_embed_dim=512, max_positions=1024))  # I have figured the numbers needed from the error messages, now it doens't display one
        # False needs to be set because else it will complain that the names are not exactly the same (one can read that they are similar)
        self.f.load_state_dict(self.checkpoint, strict=False)
        self.f = self.f.eval()  # sets the model in evaluation mode

    def getTranslatorModel(self) -> SequenceGenerator:
        # This is one way I figured from the code to make predictions whth the .genrate function from this class
        translator: SequenceGenerator = SequenceGenerator(
            self.deDic, normalize_scores=True)
        return translator


if __name__ == "__main__":
    m = Model()
    en = m.enDic
    ret = en.encode_line("Hello?")
    trans = m.getTranslatorModel()
    trans.generate([m.f], sample={"net_input": {"src_tokens":ret}})
    # m.f(ret.long(),src_lengths=8,prev_output_tokens=torch.zeros((10,10)))


"""
language_pair_dataset.py
 batch = {
        'id': id,
        'ntokens': ntokens,
        'net_input': {
            'src_tokens': src_tokens,
            'src_lengths': src_lengths,
        },
        'target': target,
        'nsentences': samples[0]['source'].size(0),
    }


monolingual_dataset.py

{
        'id': torch.LongTensor([s['id'] for s in samples]),
        'ntokens': sum(len(s['source']) for s in samples),
        
        'net_input': {
            'src_tokens': merge('source'),
            'src_lengths': torch.LongTensor([
                s['source'].numel() for s in samples
            ]),
        },
        
        'target': merge('target', is_target_list),
        'nsentences': samples[0]['source'].size(0),
    }
"""
