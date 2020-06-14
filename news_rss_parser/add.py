from news.models import News, Category
import logging


def add_to_base(img_file, news_parser_rss):

    logging.basicConfig(filename='add_to_base.log', filemode='a',
                        format='%(filename)s[LINE:%(lineno)d]# '
                               '%(levelname)-8s [%(asctime)s]  %(message)s', level=logging.WARNING)
    try:
        news_list = []
        russia = ["россия", "вроссии"]
        economic = ["экономика", "финансы", "бизнес"]
        turism = ["путешествия", "туризм"]
        sng = ["бывшийссср", "снг"]
        world = ["мир", "вмире"]
        scince = ["наукаитехника", "digital", "наука", "технологии"]
        politics = ["власть", "политика"]
        culture = ["кинократия", "культура"]

        p = news_parser_rss
        title = p['title']
        category = p['category']
        description = p['description']
        source = p['source']
        link_news = p['link']
        if p['media'] == None:
            pass
        else:
           media = p['media']

        news = News.objects.all()
        for n in news:
            news_list.append(n.title.strip().lower().replace(' ', ''))

        if title.strip().lower().replace(' ', '') not in news_list:
            new = News()
            new.title = title

            if category.lower().replace(' ', '') in russia:
                new.category_id = Category.objects.get(name='Россия').pk
                new.url_source = link_news
                new.description = description
                new.media = media
                new.icon = 'news/images/' + img_file
                new.save()

            elif category.lower().replace(' ', '') in economic:
                new.category_id = Category.objects.get(name='Экономика').pk
                new.url_source = link_news
                new.media = media
                new.description = description
                new.icon = 'news/images/' + img_file
                new.save()

            elif category.lower().replace(' ', '') in sng:
                new.category_id = Category.objects.get(name='СНГ').pk
                new.url_source = link_news
                new.media = media
                new.description = description
                new.icon = 'news/images/' + img_file
                new.save()

            elif category.lower().replace(' ', '') in turism:
                new.category_id = Category.objects.get(name='Туризм').pk
                new.url_source = link_news
                new.media = media
                new.description = description
                new.icon = 'news/images/' + img_file
                new.save()


            elif category.lower().replace(' ', '') in world:
                new.category_id = Category.objects.get(name='Мир').pk
                new.url_source = link_news
                new.description = description
                new.media = media
                new.icon = 'news/images/' + img_file
                new.save()

            elif category.lower().replace(' ', '') == "спорт":
                new.category_id = Category.objects.get(name='Спорт').pk
                new.url_source = link_news
                new.media = media
                new.description = description
                new.icon = 'news/images/' + img_file
                new.save()

            elif category.lower().replace(' ', '') in scince:
                new.category_id = Category.objects.get(name='Наука и техника').pk
                new.url_source = link_news
                new.media = media
                new.description = description
                new.icon = 'news/images/' + img_file
                new.save()

            elif category.lower().replace(' ', '') == "силовыеструктуры":
                new.category_id = Category.objects.get(name='Силовые структуры').pk
                new.url_source = link_news
                new.media = media
                new.description = description
                new.icon = 'news/images/' + img_file
                new.save()

            elif category.lower().replace(' ', '') in politics:
                new.category_id = Category.objects.get(name='Политика').pk
                new.url_source = link_news
                new.media = media
                new.description = description
                new.icon = 'news/images/' + img_file
                new.save()

            elif category.lower().replace(' ', '') in culture:
                new.category_id = Category.objects.get(name='Культура').pk
                new.url_source = link_news
                new.media = media
                new.description = description
                new.icon = 'news/images/' + img_file
                new.save()

            elif category.lower().replace(' ', '') == "происшествия":
                new.category_id = Category.objects.get(name='Происшествия').pk
                new.url_source = link_news
                new.media = media
                new.description = description
                new.icon = 'news/images/' + img_file
                new.save()

            elif category.lower().replace(' ', '') == "нацпроекты":
                new.category_id = Category.objects.get(name='Нацпроекты').pk
                new.url_source = link_news
                new.media = media
                new.description = description
                new.icon = 'news/images/' + img_file
                new.save()

            elif category.lower().replace(' ', '') == "авто":
                new.category_id = Category.objects.get(name='Авто').pk
                new.url_source = link_news
                new.media = media
                new.description = description
                new.icon = 'news/images/' + img_file
                new.save()
            else:
                pass

    except Exception as e:
        msg = category, e
        logging.error(msg)


if __name__ == '__main__':
    add_to_base()