# Generated by Django 4.0.6 on 2022-11-23 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='Ссылка'),
        ),
    ]