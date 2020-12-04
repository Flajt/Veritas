from fairseq.models.fconv import FConvEncoder, FConvDecoder
from fairseq.models.fconv_self_att import FConvModelSelfAtt
# from model import FConvModelSelfAtt, FConvEncoder, FConvDecoder Currently useless
import torch
from fairseq.data import Dictionary


class ModelApi():
    def __init__(self, deviceType: str = "cpu") -> None:
        self.ckpath: str = "src/model/ConvS2S/checkpoint_best.pt"
        self.dictPath = "./src/Fairseq_test/"
        self.deviceType: str = deviceType
        self._encoderDict = Dictionary()
        self._encoderDict.add_from_file(self.dictPath+"dict.en.txt")
        self._decoderDict = Dictionary()
        self._decoderDict.add_from_file(self.dictPath+"dict.sparql.txt")
        self.ckpoint: dict = torch.load(
            self.ckpath, map_location=torch.device(self.deviceType))
        self.model = FConvModelSelfAtt(encoder=FConvEncoder(
            self._encoderDict), decoder=FConvDecoder(self._decoderDict,embed_dim=768, out_embed_dim=512, max_positions=1024))
        self.loadedModel = self.model.load_state_dict(
            self.ckpoint["model"],strict=False)
        ret = self.model.eval()
        print(ret)
        #FConvModelSelfAtt().load_state_dict(self.ckpoint["model"])


if __name__ == "__main__":
    api = ModelApi()
