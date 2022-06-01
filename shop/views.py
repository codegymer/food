# from attr import attr
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# from numpy import sinc
from django.core.exceptions import ObjectDoesNotExist

from user.models import ShopProfile,ShopIteam,IsShopOrNot,Cart
from django.core.files.storage import FileSystemStorage



@login_required(login_url='/login')
def register(request):


    # return HttpResponse('whi')

    if request.method=='POST':
        user_id=request.user
        shop_name=request.POST.get('shopname')
        shop_holder_name=request.POST.get('shopholdername')
        # gender=request.POST.get('gender')
        about=request.POST.get('about')
        email=request.POST.get('email')
        since=request.POST.get('since')
        can_delived_online_or_not =request.POST.get('dilivery')
        images=request.FILES.get('images')
        # images=request.FILES['image'].name


        print(images)
        
        if user_id=="" or email=="" or shop_name=="" or shop_holder_name==""  or since=="" or can_delived_online_or_not=="" or about=="" or images=="":
            messages.warning(request,"don't live black field")
            return redirect('register')

        
        elif ShopProfile.objects.filter(shop_name=shop_name).exists():
            messages.warning(request,'shopname taken')
            return redirect('register')
        
        else:

            shopprofile=ShopProfile(about=about,shop_name=shop_name ,shop_holder_name=shop_holder_name,since=since,shop_pics=images,can_delived_online_or_not=can_delived_online_or_not,user=user_id)
            shopprofile.save()
            messages.success(request,'shop registered') 
            return redirect('/shop/profile')
    return render(request,'shop/register.html')


@login_required(login_url='/login')
def profile(request):
    try:
        shop_created_=IsShopOrNot.objects.get(user=request.user)
        print(shop_created_)
        if shop_created_.shop_created ==True:
            data=ShopIteam.objects.filter(user=request.user)
            # data=ShopProfile.objects.filter(user=request.user)

            context={
                "item":data,
            }
            return render(request,'shop/profile.html',context)
        else:
            return redirect('/shop/register')


    except ObjectDoesNotExist:
        return redirect('/shop/register')
        


    # return render(request,'shop/profile.html',context)
    # return HttpResponse("shkop pro")


@login_required(login_url='/login')
def ItemRegister(request):
    if request.method=='POST':

        itemname=request.POST.get('itemname')
        price=request.POST.get('price')
        about=request.POST.get('about')
        catagories=request.POST.get('catagories')
        image=request.FILES.get('image')
        # image=request.FILES['image']
        # fss = FileSystemStorage(location='/media/iteam_images')
        # filename=fss.save(image.name,image)

        # print(filename)
        # url=fss.url(filename)
        # print(url)


        # print(itemname,price,about)
        # print('name',itemname)

        if itemname=="" or price=="" or about=="" or image=="" or catagories=="":

            messages.warning(request,"don't live black field item registration")
            return redirect('iregister')
        else:
            shop=ShopProfile.objects.get(user=request.user)
            id=getattr(shop,'id')
            creat=ShopIteam(iteam_name=itemname,iteam_price=price,iteam_catogories=catagories,about=about,iteam_image=image,  user=request.user,shopprofile=shop)   
            creat.save()
          

    return render(request,'shop/item_register.html')

@login_required(login_url='/login')
def add_cart(request,id):
    user=request.user
    idd=ShopIteam.objects.get(id=id)
    # idd=id
    cart=Cart.objects.create(user=user,shopiteam=idd)
    cart.save()
    return redirect('/')

@login_required(login_url='/login')
def del_cart(request,id):
    user=request.user
    idd=ShopIteam.objects.get(id=id)
    # idd=id
    cart=Cart.objects.filter(user=user,shopiteam=idd)
    cart.delete()
    return redirect('/shop/cart')



def cart(request):
    user=request.user
    data=Cart.objects.filter(user=user).values('shopiteam_id')
    print("/////////////")
    print(data)
    print("/////////////")
    sk=ShopIteam.objects.filter(id__in=data)

    print(sk)

    # cart=ShopIteam.objects.filter(id=data)
    # print(cart)

    value={

        "allcart":sk

    }
    return render(request,'shop/cart.html',value)

def shopprofileedit(request):

    if request.method=="POST":

        sn=request.POST.get('shopname')
        shn=request.POST.get('shopholdername')
        since=request.POST.get('since')
        dilivery=request.POST.get('dilivery')
        images=request.FILES.get('images')
        about=request.POST.get('about')
        # se=request.POST.get('shopemail')
        # phone=request.POST.get('phone')
        # pin=request.POST.get('pin') 
        # state=request.POST.get('state') 

        # request.user.first_name=fname

        # us=User.objects.get(id=request.user.id)

        if images=="null":  
            return redirect('/shop/edit')
        else:

            us=ShopProfile.objects.get(user=request.user)
            us.shop_name=sn
            us.shop_holder_name=shn
            us.since=since
            us.can_delived_online_or_not=dilivery
            us.shop_pics=images
            us.about=about
        
            us.save()
            return redirect('/shop/profile')



   
    shopdata=ShopProfile.objects.get(user=request.user)

    print(shopdata)   

    data={  
        "shopdata":shopdata,        
    }
    return render(request,'shop/shop_profileedit.html',data)

