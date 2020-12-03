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
    """Contains initilaized Model"""
    def __init__(self) -> None:
        self.enDic = Dictionary()# Creates dictionary, seems to be the wrapper for embedding layers I guess
        self.deDic = Dictionary()
        self.enDic.add_from_file("tntspa/fairseq/fairseq/models/dict.en.txt")# loads the dictionary from the papers author
        self.deDic.add_from_file("tntspa/fairseq/fairseq/models/dict.sparql.txt")
        self.checkpoint = torch.load("src/model/ConvS2S/checkpoint_best.pt", map_location=torch.device('cpu'))["model"]#loads modelcheckpoint to cpu
        self.f = FConvModelSelfAtt(encoder=FConvEncoder(self.enDic,),
                        decoder=FConvDecoder(self.deDic, embed_dim=768, out_embed_dim=512, max_positions=1024))# I have figured the numbers needed from the error messages, now it doens't display one
        self.f.load_state_dict(self.checkpoint, strict=False)# False needs to be set because else it will complain that the names are not exactly the same (one can read that they are similar)
        self.f = self.f.eval()# sets the model in evaluation mode
    
    def getTranslatorModel(self)-> SequenceGenerator:
        translator:SequenceGenerator = SequenceGenerator([self.f], self.deDic,normalize_scores=True)# This is one way I figured from the code to make predictions whth the .genrate function from this class
        return translator