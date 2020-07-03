from .sarnews import SarNewsParser
from news.models import SarNews


def sar_news_parser():

    list_urls = ['https://www.vzsar.ru/rss', 'https://www.4vsar.ru/rss', 'https://saratov24.tv/rss']

    for url in list_urls:
        news_list = []
        for sar_news in SarNews.objects.all():
            sar_news = sar_news.title.lower().replace(' ', '')
            news_list.append(sar_news)

        rss = SarNewsParser(url)
        title = rss.news_title()
        if title.lower().replace(' ', '') not in news_list:
            new_news = SarNews()
            new_news.title = title
            new_news.description = rss.news_description()
            new_news.url_source = rss.news_link()
            new_news.media = rss.news_media()
            new_news.save()
