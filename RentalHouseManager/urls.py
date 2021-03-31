"""RentalHouseManager URL Configuration

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
from django.contrib import admin
from django.urls import path, include, re_path
import Manager.views
import iframe_api.views

from django.views.static import serve
from RentalHouseManager import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('user/', include('Manager.urls', namespace='user')),
    path('', Manager.views.MainPage.as_view(), name='home'),
    path('iframe_api/', include('iframe_api.urls', namespace='iframe_api')),
    re_path(r'^files/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
]

handler404 = Manager.views.page_not_found
