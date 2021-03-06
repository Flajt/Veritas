from bs4.element import SoupStrainer
from tqdm import tqdm
import requests
import bs4
class Downloader():

    def __init__(self):

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        #self.url = "https://edef3.pcloud.com/cBZXrvi57Zm5YJl7ZZZlcw5G7Z2ZZeH5ZkZQCnu87ZmZUZ2Zm7Z77ZF7ZeZ07ZlZgZwZEZoZ47ZWfW7Z3guyeVhU53hWKGIn8zfn8RkFg08V/checkpoint_best.pt"
        self.url = self._extractLink()
        self.chunk_size = 8192

    def _extractLink(self):
        """
        Extracts download link from website to prevent errors due to changing download links
        """
        shareLink = "https://e.pcloud.link/publink/show?code=XZWfW7Z1kElBAy9mgLpljy8vTHvSJpSkLP7"
        ret = requests.get(shareLink)
        html = ret.content
        decode:str = html.decode("utf-8")
        soup = bs4.BeautifulSoup(html,features="html.parser")
        getJS:str = soup.select("script")[-1].string
        linkEscaped = getJS.split('downloadlink":')[1].split(",")[0].strip('" "')#accesses the download link and cleans it up
        link = linkEscaped.replace("\\","") #remove escaped characters
        return link

    def download(self, path):
        """
        Downloads model checkpoint, please don't edit anything!
        """
        # Modified a bit from: https://stackoverflow.com/questions/37573483/progress-bar-while-download-file-over-http-with-requests#37573701
        print("[i]: Starting download...\n")
        with requests.get(self.url, stream=True, headers=self.headers) as r:
            r.raise_for_status()
            total_size_in_bytes = int(r.headers.get('content-length', 0))
            progress_bar = tqdm(total=total_size_in_bytes,
                                unit='iB', unit_scale=True)
            with open(path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=self.chunk_size):
                    progress_bar.update(len(chunk))
                    f.write(chunk)
            progress_bar.close()
