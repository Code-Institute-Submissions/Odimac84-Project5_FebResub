from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
# updating order total when adding or updating an item.
def update_on_save(sender, instance, created, **kwargs):

    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
# updating order total when deleting an item.
def update_on_delete(sender, instance, **kwargs):

    instance.order.update_total()
