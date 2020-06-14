from news.news_rss_parser.news_parser_rss import rss_parser
from news.news_rss_parser import add

url = 'https://www.gazeta.ru/export/rss/first.xml'
img = 'gazetru.jpg'


def gazetaru():
    add.add_to_base(img, rss_parser(url))
