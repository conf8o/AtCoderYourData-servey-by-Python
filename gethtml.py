import os
import zlib

from bs4 import BeautifulSoup
import requests

from config import USE_HTML_CACHE

def url_html_cache(path, use=True):
    """
    URL経由で取得したhtmlをキャッシュしておくためのデコレータ
    """
    if not os.path.exists(path):
        os.mkdir(path)
    def _url_soup_cache(func):
        def wrapper(url: str):
            ad = hex(zlib.adler32(bytes(url, "utf-8")))
            filename = f"{path}/{ad}.html"
            if os.path.exists(filename) and use:
                print("use cached history.")
                html = open(filename, encoding="utf-8").read()
            else:
                html = func(url)
                open(filename, "w", encoding="utf-8").write(html)

            return html
        return wrapper
    return _url_soup_cache
        
@url_html_cache("./cache", USE_HTML_CACHE)
def get_html(url):
    return requests.get(url).text

def get_soup(url):
    """
    URL経由でsoupを取得
    """
    html = get_html(url)
    soup = BeautifulSoup(html, "lxml")
    return soup