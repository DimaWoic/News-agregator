from bs4 import BeautifulSoup
import requests
import logging


def rss_parser(url):
    logging.basicConfig(filename='parser.log', filemode='a',
                        format='%(filename)s[LINE:%(lineno)d]# '
                               '%(levelname)-8s [%(asctime)s]  %(message)s', level=logging.WARNING)
    r = requests.get(url)
    try:
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            news_source_title = soup.find('title').text
            get_all_item = soup.find_all('item')
            get_item = soup.find('item')
            get_title = get_item.find('title').text
            get_link = get_item.find('guid').text
            try:
                get_media = get_item.find('enclosure').get('url')
            except:
                get_media = None
            try:
                get_category = get_item.find('category').text
                list_category = []
                for c in get_all_item:
                    get_all_category = c.find('category').text
                    list_category.append(get_all_category.replace(' ', '').lower())
                    all_category = list(set(list_category))
            except Exception as e:
                msg = news_source_title, e
                logging.error(msg)
                get_category = None
                all_category = None
            get_description = get_item.find('description').text
            output = {'title': get_title, 'category': get_category, 'source': news_source_title, 'link': get_link,
                      'description': get_description, 'all_category': all_category, 'media': get_media}

        return output
    except Exception as e:
        msg = news_source_title, e
        logging.error(msg)


if __name__ == '__main__':
    rss_parser()