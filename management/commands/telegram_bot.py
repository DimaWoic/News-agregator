from news.telegrambot.tbot import greetings, get_updates, news_sender
from django.core.management.base import BaseCommand, CommandError
from news.models import News, TUsers


class Command(BaseCommand):

    def handle(self, *args, **options):
        news_sender()