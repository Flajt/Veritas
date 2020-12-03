from fairseq.models.fconv import FConvModel
from model import FConvModelSelfAtt, FConvEncoder, FConvDecoder
import torch
from fairseq.data import Dictionary


class ModelApi():
    def __init__(self, deviceType: str = "cpu") -> None:
        self.ckpath: str = "src/model/ConvS2S/checkpoint_best.pt"
        self.deviceType: str = deviceType
        self.ckpoint: dict = torch.load(
            self.ckpath, map_location=torch.device(self.deviceType))
        self.model = FConvModelSelfAtt(encoder=FConvEncoder(
            Dictionary(), decoder=FConvDecoder()))
        self.loadedModel = self.model.load_state_dict(
            self.ckpoint["args"])
