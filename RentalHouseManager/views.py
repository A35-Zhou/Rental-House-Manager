from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class MainPage(View):
    def get(self, request):
        return render(request, template_name='mainpage.html')
