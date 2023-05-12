from django.urls import path, include
from .views import *

urlpatterns = [
    path('',d1, name='index'),
    path('contact/',d2, name='contact'),
    path('about/',d3, name='about'),
    path('service/',d4, name='service'),
    path('register/',d5,name='register'),
    path('register_submit/',register_submit,name='register_submit'),
    path('otp/',otp_fun,name='otp'),
    path('login/',login, name= 'login'),
    path('logout/', logout, name='logout'),
    path('add_blog/',add_blog,name='add_blog'),
    path('my_blog/',my_blog,name='my_blog'),
    path('single_blog/<int:pk>', single_blog, name='single_blog'),
    path('add_comment/<int:bid>', add_comment, name='add_comment'),
    path('donate/<int:bid>', donate, name='donate'),
    path('donate/paymenthandler/', paymenthandler, name='paymenthandler' ),
    path('search_blog/', search_blog, name='search_blog'),
    path('my_profile/', my_profile, name='my_profile')   








]



