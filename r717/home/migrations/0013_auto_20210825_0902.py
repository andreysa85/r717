# Generated by Django 3.1.7 on 2021-08-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_textabout'),
    ]

    operations = [
        migrations.AddField(
            model_name='textabout',
            name='about_us_ru_ru',
            field=models.TextField(null=True, verbose_name='Про нас'),
        ),
        migrations.AddField(
            model_name='textabout',
            name='about_us_uk_ua',
            field=models.TextField(null=True, verbose_name='Про нас'),
        ),
    ]