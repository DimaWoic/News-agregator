from news.news_rss_parser.news_parser_rss import rss_parser
from news.news_rss_parser import add

url = 'https://lenta.ru/rss'
img = 'lenta.jpg'


def lenta():
    add.add_to_base(img, rss_parser(url))