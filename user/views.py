from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required
from user.models import Order, User,IsShopOrNot,ShopIteam,ShopProfile
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from itertools import chain

# Create your views here.

def register(request):
    if request.method=='POST':

        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        
        if username=="" or email=="" or password=="" or password2=="":
            messages.warning(request,"don't live black field")
            return redirect('/register')

        elif password != password2:
            messages.warning(request,'password not match')
            return redirect('/register')
        elif User.objects.filter(username=username).exists():
            messages.warning(request,'username taken')
            return redirect('/register')
        elif User.objects.filter(email=email    ).exists():
            messages.warning(request,'email used')
            return redirect('/register')
        else:

            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            messages.success(request,'Registered! You can login now') 
            return redirect('login')
    return render(request,'user/register.html')


def login(request):
    # return HttpResponse('hello')
    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')
        if username=="" or password=="":
            messages.warning(request,"don't live black field")
            return redirect('login')
        else:
            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('profile')
            else:
                messages.info(request,'invailide user details')
        return redirect('login')
    return render(request,'user/login.html')


@login_required(login_url='/login')
def profile(request):
    try:
        shop_created_=IsShopOrNot.objects.get(user=request.user)

        print("/////////////////////////////////////////")
        print(shop_created_)
        value={
        "shopornot":shop_created_.shop_created
         }
    except ObjectDoesNotExist:
        value={
        "shopornot":None
         }

    
    return render(request,'user/profile.html',value)




def userprofileedit(request):

    if request.method=="POST":

        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        bio=request.POST.get('bio')
        bdy=request.POST.get('bday')
        dp=request.FILES.get('dp')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        pin=request.POST.get('pin') 
        state=request.POST.get('state') 

        request.user.first_name=fname

        us=User.objects.get(id=request.user.id)
        us.first_name=fname
        us.last_name=lname
        us.email=email
        us.bio=bio
        us.birth_date=bdy
        us.udp=dp
        us.address=address
        us.phone_number=phone
        us.pincode=pin
        us.state=state
        us.save()
        return redirect('profile')



   
    users=User.objects.get(id=request.user.id )

    print(users)   

    data={  
        "userdata":users,
    }
    return render(request,'user/profileedit.html',data)
    return render(request,'user/profileedit.html',data)









def default(request):
    # q=None
    if request.method=="GET":
        q=request.GET.get('query')
        if q:
            data=ShopIteam.objects.filter(Q(iteam_catogories__icontains=q) |Q(iteam_name__icontains=q))


    # if request.method==""
        else:
         data=ShopIteam.objects.all()

    context={
        "item":data,
    }

    return render(request,'index.html',context)

@login_required(login_url='/login')
def logouthere(request):
    # if request.method=='POST':
        
        logout(request)
        # messages.info(request,'logout successfully')
        return redirect('/login')






@login_required(login_url='/login')
def order(request,id):
        user=request.user
        number=request.user.phone_number
        pin=request.user.pincode
        add=request.user.address
        # add=request.user.address
        state=request.user.state
        pm='COD'
        if number=="" or pin=="" or add=="" or state=="" :
            messages.warning(request,'update your profile first')
            return redirect('/profile')
        else:

            # shopp=ShopProfile.objects.get(user=user)
            idd=ShopIteam.objects.get(id=id)
            print(idd)
            price=idd.iteam_price
            print(price)
            # idd=id
            ord=Order.objects.create(user=user,shopiteam=idd,phone=number,state=state,pincode=pin,address=add,payment_mode=pm,price=price)
            ord.save()
            return redirect('/')


# def ind_search(request):
#     if request.method=="get":
#     q=request.GET.get('query')  
#     print(q)
#     data=ShopIteam.objects.filter(Q(iteam_catogories__icontains=q) |  Q(iteam_name__icontains=q)) 
        
#     context={
#     "item":data,
# }

#     return render(request,'index.html',context)

def orders(request):
    user=request.user
    data=Order.objects.filter(user=user).values('shopiteam_id')
    print("/////////////")
    print(data)
    print("/////////////")  
    sk=ShopIteam.objects.filter(id__in=data)
    ord=Order.objects.filter(user=user)
    # c=list(chain(list(sk),list(ord)))

    # c=sk.join(ord)
    # sdd=sk | ord  

    print(list(sk))
    print("ccccccccccccccccc")
    # print(list(c))
    print("ccccccccccccccccc")

    # cart=ShopIteam.objects.filter(id=data)
    # print(cart)

    value={

        "orders":sk,
        "oi":ord,   
        # "ch":c,
        

    }
    return render(request,'user/orders.html',value)

        

        
    