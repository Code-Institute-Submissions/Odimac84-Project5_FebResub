from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe

# Create your views here.
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        message.error(request, "You havent added anything in your cart.")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    
    order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JukkFCPkuFDNEn36LyaWvCXlfcTxHkHpvLtxwh3vXvZ2iBuaIwhXMhwpwzdu8AkDVFJz7G1mY6UFIOnMD2p6iMO00vQ8OyB91',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)