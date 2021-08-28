from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect



from .models import Product, ProductCategorie, TextAbout
from .forms import SendMail
import os 
from cart.forms import CartAddProductForm

# Create your views here.

def home (request):
	data = dict()
	products = Product.objects.all()
	categories = ProductCategorie.objects.all()
	cart_product_form = CartAddProductForm()
	data['products'] = products
	data['categories_one'] = categories[:3]
	data['cart_product_form'] = cart_product_form
	return render(request, 'index.html', context=data)

def about (request):
	data = dict()
	text = TextAbout.objects.get(id=2)
	directory = '/home/andrey/test/r717/static/assets/images/foto_colag'
	files = os.listdir(directory)
	images = filter(lambda x: x.endswith('.jpg'), files)
	data['images_list'] = images
	data['text_about'] = text
	return render(request, 'about.html', context=data)

def contact (request):
	data = dict()
	if request.method == 'GET':
		send_mail_form = SendMail()
		data['send_mail_form'] = send_mail_form
	return render(request, 'contact.html',context=data)

def product_deteil(request, id:int):
	data = dict()
	product = Product.objects.get(id=id)
	cart_product_form = CartAddProductForm()
	if request.method == 'GET':
		data['product'] = product
		data['cart_product_form'] = cart_product_form
		return render(request, 'product_deteil.html', context=data)

def send_mail_office(request):
	sent = False
	if request.method == 'POST':
		form = SendMail(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name'] 
			email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message'] 
			send_mail(
				f'Сообщение с сайта, тема {subject}',
				f'{message} Контактные данные пользователя : {name}, {email}',
				'sale@eeg-ua.com', 
				['s.potapov@eeg-ua.com','s.zadorozhniy@eeg-ua.com']
			)
			sent = True 
		else:   
			form = SendMail()
			messages.add_message(request, messages.INFO, 'Ошибка')  
		return redirect('contact')


def rating_ajax (request):
	data = dict()
	if request.method == 'GET' and request.is_ajax():
		rate = request.GET.get('rating')
		product_id = request.GET.get('product_id')
		product = Product.objects.get(id=product_id)
		product.votes += 1
		product.rating = product.rating + float(rate)
		product.average_rating = product.rating / product.votes 
		product.save()
		votes = product.votes
		data['res'] = 5
		data['votes'] = votes
		return JsonResponse(data)
