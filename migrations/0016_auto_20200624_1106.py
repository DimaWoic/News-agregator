# Generated by Django 2.2 on 2020-06-24 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_tusers_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tusers',
            name='subscription',
            field=models.BooleanField(default=False, verbose_name='подписка'),
        ),
    ]
