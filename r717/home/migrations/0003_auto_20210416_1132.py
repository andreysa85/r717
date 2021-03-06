# Generated by Django 3.1.7 on 2021-04-16 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210416_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='desctiption_ru_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='desctiption_uk_ua',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Назва продукту'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_uk_ua',
            field=models.CharField(max_length=150, null=True, verbose_name='Назва продукту'),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description_ru_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Короткий опис'),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description_uk_ua',
            field=models.CharField(max_length=500, null=True, verbose_name='Короткий опис'),
        ),
        migrations.AddField(
            model_name='productcategorie',
            name='name_ru_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Категорія продукту '),
        ),
        migrations.AddField(
            model_name='productcategorie',
            name='name_uk_ua',
            field=models.CharField(max_length=150, null=True, verbose_name='Категорія продукту '),
        ),
    ]
