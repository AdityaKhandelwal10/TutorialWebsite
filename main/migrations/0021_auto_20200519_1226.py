# Generated by Django 3.0.6 on 2020-05-19 06:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20200519_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorials_content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorials_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 12, 26, 22, 59409), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorials_title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorialcategory',
            name='category',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorialcategory',
            name='category_summary',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='series',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='series_summary',
            field=models.CharField(max_length=200),
        ),
    ]
