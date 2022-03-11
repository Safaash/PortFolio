from django.urls import path
from django.contrib import admin
from resume import views
urlpatterns=[
    path('',views.index,name='index'),
    path('contact',views.contact,name="contact")
]