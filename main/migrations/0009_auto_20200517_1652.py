# Generated by Django 3.0.6 on 2020-05-17 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200517_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorials_content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorials_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 17, 16, 52, 55, 14231), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorials_title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorialcategory',
            name='category',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorialcategory',
            name='tutorial_summary',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='series',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='series_summary',
            field=models.CharField(default='', max_length=200),
        ),
    ]
