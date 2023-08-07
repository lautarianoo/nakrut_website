from .views import MainPageView, CategoryView, ServiceView, FAQView, ArticlesView, ArticleView
from django.urls import path

urlpatterns = [
    path("", MainPageView.as_view(), name="main_page"),
    path("category/<int:id>", CategoryView.as_view(), name="category_view"),
    path("service/<int:id>", ServiceView.as_view(), name="service_view"),
    path("faq", FAQView.as_view(), name="faq"),
    path("articles/", ArticlesView.as_view(), name="articles"),
    path("article/<int:id>", ArticleView.as_view(), name="article")
]