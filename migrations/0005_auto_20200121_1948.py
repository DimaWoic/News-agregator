# Generated by Django 2.2 on 2020-01-21 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20200112_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='icon',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='ссылка на картинку'),
        ),
    ]
