from app1.views import *
from django.urls import path
app_name='any_name'
urlpatterns=[path('first/',first,name='first'),
             path('second/',second,name='second'),]