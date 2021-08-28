from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail
from PIL import Image

# Create your models here.

class ProductCategorie(models.Model):
	"Опис категорії продукції"
	name = models.CharField(verbose_name='Категорія продукту ',max_length=150)

	def __str__(self):
		return self.name
		 
	class Meta:
		verbose_name = 'Категорія продукту '
		verbose_name_plural = 'Категорії продуктів '


class Product(models.Model):
	name = models.CharField(verbose_name='Назва продукту', max_length=150)
	categorie = models.ForeignKey(ProductCategorie, on_delete=models.CASCADE,verbose_name='Категорія продукту')
	short_description = models.CharField(verbose_name='Короткий опис', max_length=500)
	desctiption = models.TextField(verbose_name='Опис товару')
	rating =  models.FloatField(verbose_name='Рейтинг',default= 0)
	votes = models.IntegerField(verbose_name='Кількість голосів',default= 0)
	average_rating = models.FloatField(verbose_name='Середній рейтинг',default= 0)
	img_small= models.ImageField(verbose_name='Фото',upload_to='small_img/',blank=True,null=True)
	price = models.FloatField(verbose_name='Ціна')
	video_url = models.URLField(null=True, blank=True)
	video_url_2 = models.URLField(null=True, blank=True)
	pdf = models.FileField(upload_to='pdf/',blank=True)

	def __str__(self):
		return self.name
		
	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукти'



class TextAbout(models.Model):
	about = models.TextField(verbose_name='Про нас')

	def __str__(self):
		return self.about