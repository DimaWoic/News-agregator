from django.core.management.base import BaseCommand, CommandError
import time
from .interfax import interfax
from .lenta_ru import lenta
from .rg import rg
from .gazetaru import gazetaru




class Command(BaseCommand):

    def handle(self, *args, **options):
        interfax()
        lenta()
        rg()
        gazetaru()