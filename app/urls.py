from django.urls import path
from app import views

urlpatterns = [

    path('',views.index,name='index'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('login',views.handlelogin,name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('signup',views.handlesignup,name='handlesignup'),
    path('forgot-password/', views.forgot_password, name="forgot_password"),
    path('reset_password/<uidb64>/<token>/', views.reset_password, name='change_password'),
    path('search', views.search, name='search'),
    path('product-info/', views.productInfo, name='product-info'),
]
