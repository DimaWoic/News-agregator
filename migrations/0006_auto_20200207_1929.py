# Generated by Django 2.2 on 2020-02-07 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20200121_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='url_source',
            field=models.URLField(blank=True, max_length=1000, null=True, verbose_name='ссылка на ресурс'),
        ),
    ]
