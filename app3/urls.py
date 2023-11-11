from app3.views import * 
from django.urls import path
app_name='anyname'
urlpatterns=[path('first/',first,name="first"),
             path('second/',second,name="second"),]