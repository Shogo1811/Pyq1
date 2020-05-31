from django.urls import path

from . import views

urlpatterns = [
    path('good', views.good, name='good'),
    path('', views.index, name='index'),
]
