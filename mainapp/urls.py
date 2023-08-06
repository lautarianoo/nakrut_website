from .views import MainPageView, CategoryView
from django.urls import path

urlpatterns = [
    path("", MainPageView.as_view(), name="main_page"),
    path("category/<int:id>", CategoryView.as_view(), name="category_view")

]