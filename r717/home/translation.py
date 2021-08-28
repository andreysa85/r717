from modeltranslation.translator import register, TranslationOptions
from .models import ProductCategorie, Product, TextAbout

@register(ProductCategorie)
class ProductCategorieTranslationOptions(TranslationOptions):
	fields = ('name',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
	fields = ('name','short_description','desctiption')


@register(TextAbout)
class TextAboutTranslationOptions(TranslationOptions):
	fields = ('about',)
