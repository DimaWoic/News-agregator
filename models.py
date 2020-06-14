from django.db import models
from django.core import validators


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

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering  = ['-published']

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