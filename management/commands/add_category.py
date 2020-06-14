from news.models import Category
from django.core.management.base import BaseCommand


def add_category():
    list_category = ['Экономика', 'Туризм', 'Спорт', 'СНГ', 'Силовые структуры', 'Россия', 'Происшествия',
                 'Политика', 'Нацпроекты', 'Наука и техника', 'Мир', 'Культура', 'Интернет и СМИ',
                 'Власть', 'Авто', 'Digital', '']
    category_in_to_base = []

    for c in Category.objects.all():
        category_in_to_base.append(c.name)

    for category_name in list_category:
        if category_name not in category_in_to_base:
            category = Category()
            category.name = category_name
            category.save()
        else:
            print('Категория существует в базе.')


class Command(BaseCommand):

    def handle(self, *args, **options):
        add_category()