from django.db import models

# Create your models here.
class Questionary(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(blank=True)
    link = models.CharField(max_length=30, blank=True)
    
    ACTIVITY_CHOICES = (
        ('eco','Economy'),
        ('med','Medecine'),
        ('ind','Industry'),
        ('inf', 'IT'),
        ('spa', 'Space'),
    )

    activity = models.CharField(max_length=3, choices=ACTIVITY_CHOICES,
        help_text = 'Your activity' )
