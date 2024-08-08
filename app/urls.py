from django.urls import path
from .import views

urlpatterns=[
    path('',views.index),
    path('contact', views.contact),
    path('shop', views.shop),
    path('about', views.about),
    path('style', views.style),
    path('singlepost', views.singlepost),
    path('blog', views.blog),
    path('thankyou', views.thankyou),
    path('pro', views.pro),
    path('viewproduct', views.viewproduct, name='viewproduct'),
    path('productedit<int:id>', views.productedit, name='edit'),
    path('productdelete<int:id>',views.productdelete,name='delete'),
    path('signup', views.signup),
    path('login', views.loginpage,name='login'),
    path('logoutpage',views.logoutpage,name='logoutpage'),
    path('viewprd<int:id>',views.viewprd,name='viewprd'),
    #path('viewcart', views.viewcart, name='view'),
    path('viewitem', views.viewitem,name='viewitem'),
    #path('addcart<int:id>',views.addcart),
    # path('viewcartitem', views.viewcartitem, name='viewcartitem'),
    path('cart', views.cart,name='cart'),
    path('cartdelete<int:id>',views.cartdelete,name='delete'),
    path('addr',views.addr,name='addr'),
    path('buynow',views.buynow,name='buynow'),
    path('editaddr',views.editaddr,name='editaddr'),
    path('addressdelete', views.addressdelete, name='addressdelete'),
    path('order',views.orders,name='order'),

    # path('cartadd/<int:id>/', views.cartadd,name=cartadd),

]