from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=50)
	cost = models.DecimalField(max_digits=6, decimal_places=2)
	
