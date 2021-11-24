from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
    
    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_SUM:
        delivery = total * Decimal(settings.STANDARD_SHIPPING / 100)
        free_delivery_left = settings.FREE_DELIVERY_SUM - total
    else:
        delivery = 0
        free_delivery_left = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_left': free_delivery_left,
        'grand_total': grand_total,
        'free_delivery_sum': settings.FREE_DELIVERY_SUM,
    }

    return context
