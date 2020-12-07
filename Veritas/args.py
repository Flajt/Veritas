class Args:
    def __init__(self) ->None:
        self.data:str="./data/"
        self.source_lang ="en"
        self.path = " "
        self.target_lang="sparql"
        self.task = "translation"
        self.fp16:bool = False
        self.path:str = "./data/checkpoint_best.pt"
        self.model_overrides:str = "{}"
        self.beam:int = 5
        self.nbest:int = 1
        self.max_len_a:int = 0
        self.max_len_b:int = 200
        self.min_len:int = 1
        self.early_stop:bool = False
        self.no_beamable_mm:int = False
        self.lenpen:int = 1
        self.unkpen:int = 0
        self.replace_unk = False # Needs to be checked if that is the right input
        self.unnormalized:bool = False
        self.sampling:bool = False
        self.sampling_topk = -1
        self.sampling_temperature:float = 1.0
        self.diverse_beam_groups:int = -1
        self.diverse_beam_strength:float = .5
        self.print_alignment:bool = False
        """
        Number of sentences to process
        """
        self.buffer_size:int = 1
        self.max_tokens:int = 50 # first was 500
        self.max_sentences:int = 1#10
        self.left_pad_source:bool = True
        self.left_pad_target:bool = False
        self.no_early_stop:bool = False
        self.max_source_positions:int = 1024
        self.max_target_positions = 50 # needs check
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

