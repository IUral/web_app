from django.contrib import admin

# Register your models here.
from .models import Questionary

# Декоратор, он делает то же самое, что и метод admin.site.register(Product, ProductAdmin)
@admin.register(Questionary)      
class QuestionaryAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'age', 'email', 'activity')

#admin.site.register(Questionary)

