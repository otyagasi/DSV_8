from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.hello_world),
    path("index", views.index),
    path("myprofile",views.myprofile)
]
