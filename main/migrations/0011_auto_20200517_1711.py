# Generated by Django 3.0.6 on 2020-05-17 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200517_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorials_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 17, 17, 11, 56, 832289), verbose_name='Date Published'),
        ),
    ]