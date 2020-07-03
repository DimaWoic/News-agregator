from django.core.management.base import BaseCommand, CommandError
import time
from .interfax import interfax
from .lenta_ru import lenta
from .rg import rg
from .gazetaru import gazetaru
from news.sarnews.sarnews_parser import sar_news_parser




class Command(BaseCommand):

    def handle(self, *args, **options):
        while True:
            interfax()
            lenta()
            rg()
            gazetaru()
            sar_news_parser()
            time.sleep(5)