from django.shortcuts import render
from django.views import View
from .models import Category, Service, Article

class MainPageView(View):

    def get(self, request, *args, **kwargs):
        services = Service.objects.all()
        categories = Category.objects.all()
        return render(request, "mainapp/mainpage.html", {"services": services, "categories": categories})