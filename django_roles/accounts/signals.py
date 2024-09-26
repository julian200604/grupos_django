from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save, sender=Profile)
def add_user_to_customers_group(sender, instance, created, **kwargs):
    if created: 
        try:
            customers = Group.objects.get(name='cliente')
        except Group.DoesNotExist:
            customers = Group.objects.create(name='cliente')
            customers = Group.objects.create(name='administrador')
            customers = Group.objects.create(name='farmaceuta')
        instance.user.groups.add(customers)