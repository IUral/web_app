from django.contrib import admin


# Register your models here.
from .models import Product

# Декоратор, он делает регистрацию в админке,так же как и метод admin.site.register(Product, ProductAdmin)
@admin.register(Product)      
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'cost')

#admin.site.register(Product, ProductAdmin)