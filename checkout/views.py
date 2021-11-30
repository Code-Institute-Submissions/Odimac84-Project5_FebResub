from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        message.error(request, "You havent added anything in your cart.")
        return redirect(reverse('products'))

    order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JukkFCPkuFDNEn36LyaWvCXlfcTxHkHpvLtxwh3vXvZ2iBuaIwhXMhwpwzdu8AkDVFJz7G1mY6UFIOnMD2p6iMO00vQ8OyB91',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)