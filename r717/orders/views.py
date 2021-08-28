from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
    

            subject, from_email = f'Сообщение с сайта, заказ № {order.id}', 'sale@eeg-ua.com'
            html_content = render_to_string('mail_template.html', {'order_number': order.id,
                                                                    'first_name': order.first_name,
                                                                    'last_name': order.last_name,
                                                                    'phone': order.phone,
                                                                    'cart': cart})
            text_content = strip_tags(html_content)
            msg = EmailMultiAlternatives(subject, text_content, from_email, ['s.potapov@eeg-ua.com','s.zadorozhniy@eeg-ua.com'])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            # очистка корзины
            cart.clear()

            return render(request, 'orders/order/created.html',
                          {'order': order})
        else:
            form = OrderCreateForm
            return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form, 'report':'Error tel.'})

    else:

        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form, })


