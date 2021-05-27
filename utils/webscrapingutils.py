from urllib.request import urlopen, Request
from bs4 import BeautifulSoup, SoupStrainer

def get_page_soup(link):
    request = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    page_content = urlopen(request)
    return BeautifulSoup(page_content, "html.parser", from_encoding=page_content.info().get_param('charset'))