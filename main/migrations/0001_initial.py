# Generated by Django 4.0.6 on 2022-08-19 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('text', models.TextField(max_length=200, verbose_name='Текст новости')),
                ('image', models.ImageField(upload_to='news/', verbose_name='Изображение новости')),
            ],
        ),
    ]
