from os import initgroups
from fairseq.models.fairseq_encoder import FairseqEncoder
from fairseq.models.fairseq_decoder import FairseqDecoder
import torch
#subword-nmt
from torch import device, nn
from fairseq.models.fconv import FConvModel, FConvEncoder, FConvDecoder
from fairseq.models import FairseqModel, CompositeEncoder
"""
Just to show what I have tried, idealy I would have the working model in the modelApi.py file were I can call it with the predict function
"""



class ModelAPI():# DEPRECIATED -> The modelApi will be the one in modelApi.py for better file structure
    """Should be a wrapper to load different model in the long term"""
    def __init__(self, deviceType: str = "cpu"):
        self.deviceType: str = deviceType# is the device type default is cpu, because I'm using a laptop the other would be cuda if I'm not wrong
        self.ckpath: str = "src/model/ConvS2S/checkpoint_best.pt"#path of the checkpoint to load from the model
       # self.modelPath: str = "src/model/model.pt"# what I thought woulde be the model, but isn't
        #self.model = torch.load(
         #   self.modelPath, map_location=torch.device(self.deviceType))
        #print(type(self.model))
        self.ckpoint: dict = torch.load(
            self.ckpath, map_location=torch.device(self.deviceType))# loads checkpoint
        #self.model.load_state_dict(self.ckpoint)
    def loadhub(self):
        """Would load model from cloud, but can't be used due to errors"""
        model = torch.hub.load('pytorch/fairseq', 'conv.wmt14.en-fr',pretrained=False)#'transformer.wmt14.en-fr'
        print("model")
        #hash1 = hash(model)
        #print(model)
        print(self.ckpoint["model"].keys())#dict_keys(['args', 'model', 'optimizer_history', 'last_optimizer_state', 'extra_state'])
        print("------------------------")
        model.load_state_dict(self.ckpoint["model"])#in documentation and tutoriales this is the model_state_dict
        #hash2 = hash(model)
        #print(hash1==hash2)
        #print(model.translate("Hello, I'm Tjalf"))
        return "jo" # to check if something works, because sometimes code wouldn't execute


class Model():
    """Should be the model class later"""
    def __init__(self):
        super(Model,self).__init__()
        self.embedding = nn.Embedding()
        self. encoder = FConvEncoder()