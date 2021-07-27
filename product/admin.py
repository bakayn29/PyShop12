from django.contrib import admin

# Register your models here.
from .models import Product, Category


admin.site.register(Category)
admin.site.register(Product)

#TODO: создать категории: Smartphones(Samsung, Iphone, Xiaomi),
# Nootebooks(MackBook, ASUS, Acer), Earphones

