
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser


# add field in default user as abstract user
class User(AbstractUser):
    udp = models.ImageField(default='udp_pics/udpdefault.jpg', upload_to='udp_pics',null=True, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=12,blank=True)
    pincode = models.CharField(max_length=6, blank=True)
    address = models.CharField(max_length=500, blank=True)
    state = models.CharField(max_length=20, blank=True)



# crating profile of shop

class ShopProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,

    )

    
    about = models.CharField(max_length=60)
    shop_name = models.CharField(max_length=60)
    shop_holder_name = models.CharField(max_length=60)
    since = models.CharField(max_length=60)  # default created year
    can_delived_online_or_not = models.BooleanField(default=False)
    shop_pics= models.ImageField(default='udpdefault.jpg', upload_to='shop_pics')



class IsShopOrNot(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,

    )
    shopprofile = models.ForeignKey(
        ShopProfile,
        on_delete=models.CASCADE,

    )
    shop_created = models.BooleanField(default=False)

# item model


class ShopIteam(models.Model):

    shopprofile = models.ForeignKey(
        ShopProfile,
        on_delete=models.CASCADE,

    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,

    )
    iteam_name = models.CharField(max_length=60)

    iteam_price = models.CharField(max_length=60)
    iteam_catogories = models.CharField(max_length=60)
    date_time = models.DateTimeField(auto_now_add=True)



    about = models.CharField(max_length=60)
    iteam_image = models.ImageField(default='iteam_image.jpg', upload_to='iteam_images/')



class Order(models.Model):

    # shopprofile = models.ForeignKey(
    #     ShopProfile,
    #     on_delete=models.CASCADE,

    # )
    shopiteam = models.ForeignKey(
        ShopIteam,
        on_delete=models.CASCADE,

    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,

    )

    price = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    # delivery_status = models.CharField(max_length=2)
    payment_mode = models.CharField(max_length=10)
    # payment_status = models.CharField(max_length=10)
    date_time = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,

    )
    shopiteam = models.ForeignKey(
        ShopIteam,
        on_delete=models.CASCADE,

    )
