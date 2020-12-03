# Veritas

Veritas is an opensource fact checking tool.
It will be able to check a statment with the help of the Semantic Web, by converting text into sparql querry questions which will then be passed into a KnowledgeGraph


## TODO:
1. Getting an input (e.g. tweet, article etc.) -> Done
2. Converting the input into questions -> Work in progress
3. Converting the questions into a Sparql query (using later FactForge as endpoint) -> Work in progress
4. Getting the answer and formatting it into a usefull answer -> Work in progress
5. Return it to the user -> Work in progress


## Where does what happen?
The `src` folder would be the theoretical folder of all code.
For testing I donwloaded the papers authors code tested there aswell, my code there can be found in `tntspa/fairseq/fairseq/models` and then `model.py` and `modelApi.py`
The goal is to have everything happen in the src folder!

## Extra stuff:
The `checkpoint_best.pt` file needs to be placed under `src/model/ConvS2S` and can be dowloaded from the tntspa repository (we used the Monument Dataset one). They can be found under the README.md in the tntspa folder or here: https://github.com/xiaoyuin/tntspa under `Trained Models` (Model used `ConvS2S` on `Monument Dataset`)


Citation:
@article{DBLP:journals/corr/abs-1906-09302,
  author    = {Xiaoyu Yin and
               Dagmar Gromann and
               Sebastian Rudolph},
  title     = {Neural Machine Translating from Natural Language to {SPARQL}},
  journal   = {CoRR},
  volume    = {abs/1906.09302},
  year      = {2019},
  url       = {http://arxiv.org/abs/1906.09302},
  archivePrefix = {arXiv},
  eprint    = {1906.09302},
  timestamp = {Thu, 27 Jun 2019 18:54:51 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1906-09302.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}