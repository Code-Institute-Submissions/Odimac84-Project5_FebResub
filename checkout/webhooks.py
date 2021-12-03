from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe

@require_POST
@csrf_exempt
def webhook(request):
    """Lister for webhooks from Stripe"""
    #SETUP importing keys
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    #getting webhook data and verification
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, wh_secret
        )
    # Invalid payload
    except ValueError as e:
        return HttpResponse(status=400)

    # Invalid signature
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    except Exception as e:
        return HttpResponse(content=e, status=400)

    handler = StripeWH_Handler(request)

    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }
    # to webhook type from stripe
    event_type = event['type']

    # getting the correct handler from stripe, set to use generic one as default.
    event_handler = event_map.get(event_type, handler.handle_event)

    #calling the event_handler with the event
    response = event_handler(event)
    return response
