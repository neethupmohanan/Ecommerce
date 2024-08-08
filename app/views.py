from django.conf.urls.static import static
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect




from .models import product, Cart, address,order


# Create your views here.
def index(request):
   return render(request,'index.html')


def about(request):
   return render(request, 'about.html')


def contact(request):
   return render(request, 'contact.html')


def shop(request):
   return render(request, 'shop.html')


def thankyou(request):
   return render(request, 'thank-you.html')


def style(request):
   return render(request, 'style.html')

def blog(request):
   return render(request, 'blog.html')

def singlepost(request):
   return render(request, 'single-post.html')


def pro(request):
   d = product.objects.all
   if request.method == 'POST':
      proname = request.POST['proname']
      print(proname)

      price = request.POST['price']
      print(price)

      image=request.FILES['image']
      print(image)

      quantity = request.POST['quantity']
      print(quantity)

      f = product.objects.create(proname=proname, price=price, quantity=quantity,image=image)
      f.save()
   return render(request, 'product.html', {'e': d})


def viewproduct(request):
   x = product.objects.all()
   return render(request, 'edit.html', {'y': x})


def productedit(request, id):
   a = product.objects.get(id=id)
   if request.method == 'POST':
      a.proname = request.POST['proname']
      a.price = request.POST['price']
      a.image = request.FILES['image']
      a.quantity = request.POST['quantity']
      a.save()
      return redirect('viewproduct')
   return render(request, 'editproduct.html', {'b': a})


def productdelete(request, id):
   a = product.objects.get(id=id)
   a.delete()
   return redirect('pro')


def signup(request):
   if request.method == 'POST':
      firstname = request.POST['firstname']
      print(firstname)

      lastname = request.POST['lastname']
      print(lastname)

      phone = request.POST['phone']
      print(phone)

      address = request.POST['address']
      print(address)

      email = request.POST['email']
      print(email)

      password = request.POST['pass']
      username = request.POST['email']
      user = User.objects.create_user(username, email, password)
      user.save()
      return redirect('login')


   return render(request, 'signup.html')


def loginpage(request):
   if request.method == 'POST':
      userid = request.POST['email']
      print(userid)

      passw = request.POST['pass']
      print(passw)
      user = authenticate(username=userid, password=passw)
      if user is not None:
         login(request, user)
         print('login')
      else:
         print('incorrect')
      return redirect('index')

   return render(request,'login.html')

def logoutpage(request):
   logout(request)
   return render(request, 'login.html')

#def cartitem(request,id):
#a=Cart.objects.all()
   #a.save()
   #return render(request, 'addcart.html', {'y':a})
def viewitem(request):
   x = product.objects.all()
   return render(request, 'item.html', {'y': x})

def viewprd(request, id):
   a = product.objects.get(id=id)
   print(a)
   if request.method == 'POST':
      print('success')
      f = Cart.objects.create(products=a, price=a.price, image=a.image, quantity=1, user=request.user)
      f.save()
      return redirect('viewprd', id=id)
   return render(request, 'cart.html', {'b': a})

def cart(request):
   y=Cart.objects.all()
   return render(request,'cartitem.html',{'u':y})

   #def viewcart(request):
      #a = Cart.objects.all()
      #if request.method == 'POST':
         #a.productname = request.POST['productname']
   # a.price = request.POST['price']
   # a.image = request.POST['image']
   #     a.quantity = request.POST['quantity']
   #    a.save()
   # return render(request, 'cartitem.html', {'b': a})


def viewitem(request):
   x = product.objects.all()
   return render(request, 'item.html', {'y': x})







# def cartadd(request):
#    product = product.objects.get(id=id)
#    cart_item, created = cartitem.objects.get_or_create(product=product,
#                                                        user=request.user)
#    cart_item.quantity += 1
#    cart_item.save()
#
#    return redirect('cartdetail')


#def addcart(request,id):
   # a=Cart.objects.get(id=id)

   #return redirect('viewprd')


#def viewcartitem(request):
   # cart_id = request.session.get('cart_id')
   # c = Cart.objects.get(id=cart_id) if cart_id else None
   # t = sum(item.productname.price * item.quantity for item in Cart.objects.all()) if Cart else 0
   #return render(request, 'cartviewcart.html', {'a': c,'s': t})

def cartdelete(request,id):
   a = Cart.objects.get(id=id)
   a.delete()
   return redirect('cart')

def addr(request):
   a = address.objects.all()
   if request.method == 'POST':

      housename= request.POST['housename']
      print(housename)

      roadname= request.POST['roadname']
      print(roadname)

      pincode= request.POST['pincode']
      print(pincode)

      city = request.POST['city']
      print(city)


      state= request.POST['state']
      print(state)

      contact=request.POST['contact']
      print(contact)


      f = address.objects.create(user=request.user,housename=housename, roadname=roadname, pincode=pincode, city=city ,state=state, contact=contact)
      f.save()
      return redirect('buynow')

   return render(request,'address.html', {'e':a})

def buynow(request):
   c = address.objects.filter(user=request.user)
   a = Cart.objects.filter(user=request.user)
   return render(request,'buynow.html',{'b':a,'d':c})


def editaddr(request):
   a=address.objects.get(user=request.user)
   if request.method=='POST':
      a.housename=request.POST['housename']
      a.roadname=request.POST['roadname']
      a.pincode=request.POST['pincode']
      a.city=request.POST['city']
      a.state=request.POST['state']
      a.contact=request.POST['contact']
      a.save()
      return redirect('buynow')
   return render(request,'editaddress.html',{'b':a})

def addressdelete(request):
   a = address.objects.all()
   a.delete()
   return redirect('buynow')

def orders(request):
   a=address.objects.get(user=request.user)
   print(a)
   b=Cart.objects.filter(user=request.user)


   for i  in b:
      c=order.objects.create(products=i.products,address=a, user=request.user, price=i.price,quantity=i.quantity)
      c.save()
   b.delete()
   return redirect('buynow')








   #a=product.object.get(id=id)
   #print(a)
   #c=address.object.get(user=request.user)
   # request.method=='POST':
      #f=order.objects.create(products=a, price=a.price,  quantity=1, user=request.user)
      #f.save()
      #return redirect('order', id=id)
# return render('order.html',{'b':a,'d':c })




