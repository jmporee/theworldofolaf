from django.urls import path
from olafweb import views
from django.conf.urls import url

urlpatterns = [

    path('welcome', views.home),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    path('', views.login),
    path('login', views.login)
]