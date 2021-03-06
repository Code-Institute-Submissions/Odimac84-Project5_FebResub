from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
    )
from products.models import Product
from django.contrib import messages


def view_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    # adding a specified quantity of an item to the cart

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated quantity  {product.name} to {cart[item_id]} in your bag')
    else:
        cart[item_id] = quantity
        messages.success(request, f'{product.name} has been added to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def change_cart(request, item_id):
    # Adjust the quantity of a product

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated quantity  {product.name} to {cart[item_id]} in your bag')
    else:
        cart.pop(item_id)
        messages.success(request, f'{product.name} has been removed from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    # removing an item from the cart

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'{product.name} has been removed from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
