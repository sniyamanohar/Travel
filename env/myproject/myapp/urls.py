"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),

    path('place',views.place,name='place'),
path('place2',views.place2,name='place2'),
path('place1',views.place1,name='place1'),
path('place3',views.place3,name='place3'),
path('place4',views.place4,name='place4'),
path('place5',views.place5,name='place5'),
path('place6',views.place6,name='place6'),
path('place7',views.place7,name='place7'),
    path('package',views.package,name='package'),
    path('contact',views.contact,name='contact'),
]