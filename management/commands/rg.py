from news.news_rss_parser.news_parser_rss import rss_parser
from news.news_rss_parser import add

url = 'https://rg.ru/xml/index.xml'
img = 'rg.jpg'


def rg():
    add.add_to_base(img, rss_parser(url))