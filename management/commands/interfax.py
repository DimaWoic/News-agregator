from news.news_rss_parser.news_parser_rss import rss_parser
from news.news_rss_parser import add

url = 'https://www.interfax.ru/rss.asp'
img = 'interfax.jpg'


def interfax():
    add.add_to_base(img, rss_parser(url))