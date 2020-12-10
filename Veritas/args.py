from Veritas import get_data
class Args:
    def __init__(self) ->None:
        """
        Path to the folder containing the vocabulary
        """
        self.data:str=get_data("dicts/")
        """
        The language from which will be the input
        """
        self.source_lang ="en"
        """
        Output language
        """
        self.target_lang="sparql"
        """
        What our task is, default translation
        """
        self.task = "translation"
        """
        If we want to use fp16, default is False
        """
        self.fp16:bool = False
        """
        Path to checkpoint
        """
        self.path:str = get_data("checkpoint_best.pt")
        """
        A dictionary used to override model args at generation that were used during model training, default "{}"
        """
        self.model_overrides:str = "{}"
        """
        Beam size, default 5
        """
        self.beam:int = 5
        """
        Number of hypothisis to output, default 1
        """
        self.nbest:int = 1
        """
        generate sequences of maximum length ax + b, where x is the source length, default 0
        """
        self.max_len_a:int = 0
        """
        generate sequences of maximum length ax + b, where x is the source length, default 200
        """
        self.max_len_b:int = 200
        """
        minimum generation length, default 1
        """
        self.min_len:int = 1
        """
        If we need to stop early or not, default False
        """
        self.early_stop:bool = False
        """
        """
        self.no_beamable_mm:int = False
        """
        """
        self.lenpen:int = 1
        """
        """
        self.unkpen:int = 0
        """
        """
        self.replace_unk = False # Needs to be checked if that is the right input
        """
        """
        self.unnormalized:bool = False
        """
        """
        self.sampling:bool = False
        """
        """
        self.sampling_topk = -1
        """
        """
        self.sampling_temperature:float = 1.0
        """
        """
        self.diverse_beam_groups:int = -1
        """
        """
        self.diverse_beam_strength:float = .5
        """
        """
        self.print_alignment:bool = False
        """
        Number of sentences to process
        """
        self.buffer_size:int = 1
        """
        """
        self.max_tokens:int = 25 # first was 500
        """
        """
        self.max_sentences:int = 2#10
        """
        """
        self.left_pad_source:bool = True
        """
        """
        self.left_pad_target:bool = False
        """
        """
        self.no_early_stop:bool = False
        """
        """
        self.max_source_positions:int = 1024
        """
        """
        self.max_target_positions = 50 # needs check
        """
        
        """
        self.remove_bpe:str = "none"
        """
            "task":"translation",
            "fp16":False,
            "path":self.m.chkpath,
            "model_overrides":{},
            "beam":5,
            "nbest":1,
            "max_len_a":0,
            "max_len_b":200,
            "min_len":1,
            "no_early_stop": False,
            "no-bemable-mm":False,
            "lenpen":1,
            "unkpen": 0,
            "replace-unk":False, #"Check"
            "unnormalized":False,
            "sampling":False,
            "sampling-topk":-1,
            "sampling_temperature": 1.0,
            "diverse-beam-groups":-1,
            "diverse_beam_strength":0.5,
            "print_alignment":False,
            "buffer_size":10,
            "max_tokens":500, #custom
            "max_sentences":10,
            "task":"translation"
        
        """

