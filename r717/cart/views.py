from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from home.models import Product
from .cart import Cart
from .forms import CartAddProductForm

from django.http import JsonResponse, HttpResponseRedirect


def ajax_cart_plus(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	cart.add(product=product)
	count = cart.my_len()
	data = dict()
	data["result"] = 'ok'
	data["count"] = count
	return JsonResponse(data)

@require_POST
def cart_add(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	form = CartAddProductForm(request.POST)
	if form.is_valid():
	    cd = form.cleaned_data
	    cart.add(product=product,
	             quantity=cd['quantity'],
	             update_quantity=cd['update'])
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def cart_plus(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	cart.add_plus(product=product)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def cart_minus(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	cart.cart_minus(product=product)
	return redirect('cart_detail')

def cart_remove(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	cart.remove(product)
	return redirect('cart_detail')

def cart_detail(request):
	cart = Cart(request)
	return render(request, 'cart/detail.html', {'cart': cart})
