
from django.urls import path
from shop.views import register,profile, ItemRegister,add_cart,cart,del_cart,shopprofileedit

urlpatterns = [
    path('register', register, name='register'),
    path('profile', profile , name='prfile'),
    path('iregister', ItemRegister , name='iregister'),
    path('addcart/<id>', add_cart , name='add_cart'),
    path('deletecart/<id>', del_cart , name='del_cart'),
    path('cart', cart , name='cart'),
    path('edit', shopprofileedit , name='cart'),

    
]
