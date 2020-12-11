import os
from Veritas import downloader

_ROOT = os.path.abspath(os.path.dirname(__file__))
def get_data(path):
    return os.path.join(_ROOT, 'data', path)
#https://stackoverflow.com/questions/4519127/setuptools-package-data-folder-location#5423147
if not os.path.exists(get_data("checkpoint_best.pt")):
    d = downloader.Downloader()
    d.download(path=get_data("checkpoint_best.pt"))
    os.system("python -m spacy download en_core_web_sm")
    print("Download completed!\n")


__version__="0.0.6"

