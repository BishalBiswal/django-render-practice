from django.db import models

# Create your models here.
class CoffeeBeans(models.Model):
    varietal = models.CharField(max_length=200)
    elevation = models.IntegerField()
    notes = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title