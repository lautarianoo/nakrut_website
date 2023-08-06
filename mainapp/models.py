from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):

    title = models.CharField(verbose_name="Название категории", max_length=100)
    img = models.ImageField(verbose_name="Иконка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural="Категории"

class Service(models.Model):

    title = models.CharField(verbose_name="Название услуги", max_length=100)
    img = models.ImageField(verbose_name="Иконка")
    quantity = models.CharField(verbose_name="Количество накрутки (от и до)", help_text="Например: 1 тыс. - 900 тыс.", blank=True, null=True, max_length=60)
    warranty = models.CharField(verbose_name="Гарантия", help_text="Например: 12 мес.", blank=True, null=True, max_length=50)
    description = RichTextUploadingField(verbose_name="Описание")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, blank=True, null=True, related_name="services")

    def __str__(self):
        return f"{self.title} | {self.category.title}"

    class Meta:
        verbose_name="Услуга"
        verbose_name_plural="Услуги"

class Article(models.Model):

    title = models.CharField(verbose_name="Название статьи", max_length=100)
    img = models.ImageField(verbose_name="Иконка")
    description = RichTextUploadingField(verbose_name="Контент статьи")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Статья"
        verbose_name_plural="Статьи"