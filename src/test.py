from fairseq.data import Dictionary
from fairseq.models.fconv import FConvDecoder, FConvEncoder
from fairseq.models.fconv_self_att import FConvModelSelfAtt
import torch

model = FConvModelSelfAtt(encoder=FConvEncoder(Dictionary()),decoder=FConvDecoder(Dictionary()))
model.load_state_dict(torch.load("src/model/ConvS2S/checkpoint_best.pt",map_location=torch.device('cpu'))["model"],strict=False)
print("error")