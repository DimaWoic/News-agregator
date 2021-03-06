# Generated by Django 2.2 on 2020-02-27 17:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='email',
            field=models.EmailField(max_length=20, validators=[django.core.validators.EmailValidator(message='Введите коректный адрес электронной почты')], verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MaxLengthValidator(0, message='Введите Ваше имя')], verbose_name='Имя отправителя'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='text',
            field=models.TextField(max_length=500, validators=[django.core.validators.MaxLengthValidator(500, message='Допустимое количество символов привысило 500'), django.core.validators.MinLengthValidator(0, message='Введите сообщение')], verbose_name='Текст сообщения'),
        ),
    ]
