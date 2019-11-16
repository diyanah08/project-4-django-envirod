from django.db import models
from accounts.models import MyUser

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255, blank=False)
    sku = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    cost = models.IntegerField(blank=False)
    image = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.name + " : " + self.sku
        
    def getCostInDollars(self):
        return self.cost/100

class Item(models.Model):
    personalise = models.CharField(max_length=30, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # # photos = models.ImageField(upload_to='images/', null=True)
    # photos= ImageField(null=True)
    quantity = models.IntegerField(blank=False, default=0)
    
    def __str__(self):
        return self.personalise + " x " + str(self.quantity)
    
    def getTotalCost(self):
        return (self.category.cost * self.quantity)/100