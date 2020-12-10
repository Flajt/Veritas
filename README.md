# Veritas
(Package name is Veritass due to namespace problems)
Veritas is an opensource fact checking tool.
It will be able to check a statment with the help of the Semantic Web, by converting text into sparql querry questions which will then be passed into a KnowledgeGraph.


## TODO:
1. Getting an input (e.g. tweet, article etc.) -> Done
2. Converting the input into questions -> Work in progress
3. Converting the questions into a Sparql query (using later FactForge as endpoint) -> Done
4. Getting the answer and formatting it into a usefull answer -> Work in progress
5. Return it to the user -> Done


## Installation:
It's a package so you can import it (disclaimer: still in development).<br/>
*For development*:`pip install -e ./Veritas` (by pulling it from here) and pull yourself the tntspa repository and initalise the submodules, so you have the version of fairseq we use for development<br/>

All code can be currently found in the `Veritas` folder <br/>
*For using it*: `pip install Veritass` <br/>


## Quickstart:
```from Veritas import modelApi
    m = modelApi.ModelApi()
    ret:list = m.translate(text="What is the biggest Mountin in the US? What is the capital of China?")
    print(ret)
```
## Know Issues:
Often a question won't return an answer or an related answer, we are working on it. (As you can see in the example)

## Extra stuff:
We use the model checkpoint and a code snippet from: https://github.com/xiaoyuin/tntspa and the included fairseq submodule.


## Citation:

``` @article{DBLP:journals/corr/abs-1906-09302,
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
} ```
``` @inproceedings{ott2019fairseq,
  title = {fairseq: A Fast, Extensible Toolkit for Sequence Modeling},
  author = {Myle Ott and Sergey Edunov and Alexei Baevski and Angela Fan and Sam Gross and Nathan Ng and David Grangier and Michael Auli},
  booktitle = {Proceedings of NAACL-HLT 2019: Demonstrations},
  year = {2019},
} ```