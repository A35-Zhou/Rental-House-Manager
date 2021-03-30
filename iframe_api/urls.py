"""iframe_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path
from iframe_api import views

app_name = 'iframe_api'
urlpatterns = [
    path('account/', login_required(views.Account.as_view()), name='account'),
    path('userdetail/', login_required(views.UserDetail.as_view()), name='userdetail'),
    path('mgrhome/', login_required(views.Home.as_view()), name='home'),
    path('houseinfo/', login_required(views.HouseInfo.as_view()), name='houseinfo'),
    path('roominfo/', login_required(views.RoomInfo.as_view()), name='roominfo'),
    path('typeinfo/', login_required(views.TypeInfo.as_view()), name='typeinfo'),
    path('neworder/', login_required(views.NewOrder.as_view()), name='neworder'),
    path('userorder/', login_required(views.UserOrder.as_view()), name='userorder'),
]
