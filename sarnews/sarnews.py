import requests
from bs4 import BeautifulSoup
import asyncio

#u ='https://www.vzsar.ru/rss'
#u = 'https://www.4vsar.ru/rss'
u ='https://saratov24.tv/rss'

list_urls = ['https://www.vzsar.ru/rss', 'https://www.4vsar.ru/rss', 'https://saratov24.tv/rss']

class SarNewsParser():

    def __init__(self, url):
        self.url = url
        r = requests.get(url).text
        soup = BeautifulSoup(r, 'html.parser')
        item = soup.find('item')
        self.soup = soup
        self.item = item

    def get_title_channel(self):
        title = self.soup.find('title').text
        return title

    def get_link_channel(self):
        link = self.soup.find('link').text
        return link

    def news_title(self):
        n_title = self.item.find('title').text
        return n_title

    def news_link(self):
        try:
            n_link = self.item.find('guid').text
            return n_link
        except:
            n_link = self.item.find('amplink').text
            return n_link

    def news_description(self):
        n_description = self.item.find('description').text
        return n_description

    def news_media(self):
        n_media = self.item.find('enclosure').get('url')
        return n_media


async def vzsar_ru():
    rss = SarNewsParser(list_urls[0])
    await asyncio.sleep(0)
    print(rss.news_title(), ' ', rss.get_title_channel())


async def vsar():
    rss = SarNewsParser(list_urls[1])
    await asyncio.sleep(0)
    print(rss.news_title(), ' ', rss.get_title_channel())


async def sartf():
    rss = SarNewsParser(list_urls[2])
    await asyncio.sleep(0)
    print(rss.news_title(), ' ', rss.get_title_channel())


ioloop = asyncio.get_event_loop()

tasks = [ioloop.create_task(vzsar_ru()), ioloop.create_task(vsar()), ioloop.create_task(sartf())]
wait = asyncio.wait(tasks)
ioloop.run_until_complete(wait)
ioloop.close()