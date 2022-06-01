
from django.dispatch import receiver
from django.db.models.signals import post_save
from requests import request
from user.models import ShopProfile
from user.models import User,IsShopOrNot

@receiver(post_save,sender=ShopProfile)
def update_user_profile_created_after_save_shopprofile(sender,instance,created,**kwargs):
    if created:
        user=instance.user
        shop_created=True
        IsShopOrNot.objects.create(shopprofile=instance,user=user,shop_created=shop_created)
        