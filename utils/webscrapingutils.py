from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

async def get_page_soup(link):
    user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    request = Request(link, headers=user_agent)
    page_content = urlopen(request)
    return BeautifulSoup(page_content, "html.parser", from_encoding=page_content.info().get_param('charset'))