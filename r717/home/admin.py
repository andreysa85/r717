from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from modeltranslation.admin import TranslationAdmin

from .models import ProductCategorie, Product, TextAbout 
# Register your models here.



class ProductAdminForm(forms.ModelForm):
    desctiption_uk_ua = forms.CharField(widget=CKEditorUploadingWidget())
    desctiption_ru_ru = forms.CharField(widget=CKEditorUploadingWidget())

    short_description_uk_ua = forms.CharField(widget=CKEditorUploadingWidget())
    short_description_ru_ru = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Product
        fields ='__all__'


class ProductAdmin(TranslationAdmin):
	"""docstring for ClassName"""
	list_display = ('id','name', 'categorie','rating', 'short_description', 'desctiption',
		'img_small', 'price', 'video_url','video_url_2', 'pdf')
	form = ProductAdminForm


	def __str__(self):
		return self.name



class ProductCategorieAdminForm(forms.ModelForm):
	name_uk_ua = forms.CharField(widget=CKEditorWidget())
	name_ru_ru = forms.CharField(widget=CKEditorWidget())
	class Meta:
		model = ProductCategorie
		fields ='__all__'

class ProductCategorieAdmin(TranslationAdmin):
	list_display = ('id','name')
	form = ProductCategorieAdminForm



class TextAboutAdminForm(forms.ModelForm):
	about_uk_ua = forms.CharField(widget=CKEditorWidget())
	about_ru_ru = forms.CharField(widget=CKEditorWidget())
	class Meta:
		model = TextAbout
		fields ='__all__'

class TextAboutAdmin(TranslationAdmin):
	list_display = ('about',)
	form = TextAboutAdminForm

		
admin.site.register(ProductCategorie,ProductCategorieAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(TextAbout,TextAboutAdmin)