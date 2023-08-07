from django.shortcuts import render
from django.views import View
from .models import Category, Service, Article

class MainPageView(View):

    def get(self, request, *args, **kwargs):
        services = Service.objects.all()
        categories = Category.objects.all()
        return render(request, "mainapp/mainpage.html", {"services": services, "categories": categories})

class CategoryView(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        category = Category.objects.get(id=kwargs.get("id"))
        services = Service.objects.filter(category=category)
        return render(request, "mainapp/category.html", {"services": services, "categories": categories, "category": category})

class ServiceView(View):

    def get(self, request, *args, **kwargs):
        service = Service.objects.get(id=kwargs.get("id"))
        context = {"service": service}
        rec_services = Service.objects.all()
        recommended = []
        for rec_service in rec_services:
            if rec_service != service:
                recommended.append(rec_service)
        if recommended:
            context["rec_services"] = recommended[0]
        else:
            context["rec_services"] = None
        return render(request, "mainapp/service.html", context)

class FAQView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "mainapp/faq.html", {})

class ArticlesView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, "mainapp/articles.html", {"articles": articles})

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = Article.objects.get(id=kwargs.get("id"))
        context = {"article": article}
        recommended = []
        articles = Article.objects.all()
        for rec_article in articles:
            if article != rec_article:
                recommended.append(rec_article)
        if recommended:
            context["rec_article"] = recommended[0]
        else:
            context["rec_article"] = None
        return render(request, "mainapp/article.html", context)