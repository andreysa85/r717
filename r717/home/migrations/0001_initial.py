# Generated by Django 3.1.7 on 2021-03-17 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категорія продукту ')),
            ],
            options={
                'verbose_name': 'Категорія продукту ',
                'verbose_name_plural': 'Категорії продуктів ',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Назва продукту')),
                ('short_description', models.TextField()),
                ('desctiption', models.TextField()),
                ('rating', models.PositiveSmallIntegerField()),
                ('img_small', models.ImageField(blank=True, null=True, upload_to='small_img/')),
                ('price', models.FloatField()),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.productcategorie', verbose_name='Категорія продукту')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукти',
            },
        ),
    ]
