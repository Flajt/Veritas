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
It's a package so you can import it (still in development tho).
All code can be found in the `Veritas` folder
In `src` you can find main.py which is only for development

## Extra stuff:
The `checkpoint_best.pt` file needs to be placed under `data` and can be dowloaded from the tntspa repository (we used the Monument Dataset one). They can be found under the README.md in the tntspa folder or here: https://github.com/xiaoyuin/tntspa under `Trained Models` (Model used `ConvS2S` on `Monument Dataset`)


## Citation:

```@article{DBLP:journals/corr/abs-1906-09302,
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
}```