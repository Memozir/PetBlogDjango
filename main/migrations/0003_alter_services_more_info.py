# Generated by Django 4.0.6 on 2022-11-23 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_services_more_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='more_info',
            field=models.TextField(blank=True, max_length=650, verbose_name='Подробнее'),
        ),
    ]
