from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from .models import Car, CarInventory
from edenai_api.edenai_request import get_ai_description_car

def cars_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.description:
        ai_description = get_ai_description_car(instance.model, instance.brand, instance.model_year)
        instance.description = ai_description
    

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    cars_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    cars_inventory_update()
