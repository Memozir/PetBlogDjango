# Generated by Django 4.0.6 on 2022-11-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='more_info',
            field=models.TextField(blank=True, max_length=650, verbose_name='Подробнее'),
        ),
    ]