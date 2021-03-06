# Generated by Django 3.0.6 on 2020-05-14 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorials_title', models.CharField(max_length=200)),
                ('tutorials_content', models.TextField()),
                ('tutorials_published', models.DateTimeField(verbose_name='Date Published')),
            ],
        ),
    ]
