from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='more_info',
            field=models.TextField(blank=True, max_length=600, verbose_name='Подробнее'),
        ),
    ]
