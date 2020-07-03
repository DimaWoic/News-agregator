from django.db import models
from django.core import validators
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
import smtplib
from email.message import EmailMessage




class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='категория')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['-name']

    def __str__(self):
        return self.name


class News(models.Model):
    published = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300, verbose_name='Заголовок', blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', blank=True, default='', related_name='entries', on_delete=models.CASCADE)
    icon = models.CharField(max_length=1000, verbose_name='ссылка на картинку', blank=True, null=True)
    description = models.TextField(editable=False, verbose_name='Текст новости', blank=True, null=True)
    url_source = models.URLField(max_length=1000, verbose_name='ссылка на ресурс', blank=True, null=True)
    media = models.URLField(max_length=1000, verbose_name='Ссылка на медиа', blank=True, null=True)

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering  = ['-published']

    def __str__(self):
        return self.title


class SarNews(models.Model):
    published = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300, verbose_name='Заголовок', blank=True)
    description = models.TextField(editable=False, verbose_name='Текст новости', blank=True, null=True)
    url_source = models.URLField(max_length=1000, verbose_name='ссылка на новость', blank=True, null=True)
    media = models.URLField(max_length=1000, verbose_name='Ссылка на медиа', blank=True, null=True)

    class Meta:
        verbose_name = 'новости Саратова'
        verbose_name_plural = 'новости Саратова'
        ordering = ['-published']

    def __str__(self):
        return self.title


class Messages(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя отправителя', null=False, blank=False, validators=[validators.MaxLengthValidator(20,message='Введите Ваше имя')])
    email = models.EmailField(max_length=100, verbose_name='Электронная почта', null=False, blank=False, validators=[validators.EmailValidator(message='Введите коректный адрес электронной почты')])
    text = models.TextField(max_length=500, verbose_name='Текст сообщения', null=False, blank=False, validators=[validators.MaxLengthValidator(500, message='Допустимое количество символов привысило 500'), validators.MinLengthValidator(0, message='Введите сообщение')])
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ['-published']


class TUsers(models.Model):
    user_id = models.IntegerField(verbose_name='ID Пользователя телеграм')
    user = models.CharField(max_length=100, verbose_name='ник')
    subscription = models.BooleanField(verbose_name='подписка', null=True, blank=True)

    class Meta:
        verbose_name = 'пользователь телеграмм'
        verbose_name_plural = 'пользователи телеграмм'

    def __str__(self):
        self.user


def news_sender():
    url = 'https://api.telegram.org/bot1263816311:AAHtoS8SYIDL6i1LBPH8Csmf7k985MbpcgA/'
    news = News.objects.first()
    msg_title = news.title
    msg_source = news.url_source
    requests.get(url + 'sendMessage?chat_id=' + '@rumagpie' + '&text=' + msg_title + "\n" + msg_source)

@receiver(post_save, sender=News)
def message_sender(sender, **kwargs):
    if kwargs['created']:
        pass
        #news_sender()

def sar_news_sender():
    url = 'https://api.telegram.org/bot1263816311:AAHtoS8SYIDL6i1LBPH8Csmf7k985MbpcgA/'
    news = SarNews.objects.first()
    msg_title = news.title
    msg_source = news.url_source
    requests.get(url + 'sendMessage?chat_id=' + '@rumagpie_sar' + '&text=' + msg_title + "\n" + msg_source)

@receiver(post_save, sender=SarNews)
def sar_message_sender(sender, **kwargs):
    if kwargs['created']:
        pass
        #sar_news_sender()

def send_email():

    sender_msg = Messages.objects.first()

    fromaddr = "tovary164@yandex.ru"
    toaddrs = "wdv85@mail.ru"
    subject = "rumagpie.ru: У Вас новое сообщение от " + sender_msg.name

    text = sender_msg.name + '[' + sender_msg.email + ']' + ':' + '\n' + sender_msg.text

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = fromaddr
    msg["To"] = toaddrs

    msg.set_content(text)

    server = smtplib.SMTP_SSL(host='smtp.yandex.ru', port=465)
    server.login(user='tovary164', password='zypvnpthaqsqgsbt')
    server.sendmail(from_addr=fromaddr, to_addrs=toaddrs, msg=msg.as_string())
    server.close()

@receiver(post_save, sender=Messages)
def msg_notification(sender, **kwargs):
    if kwargs['created']:
        send_email()