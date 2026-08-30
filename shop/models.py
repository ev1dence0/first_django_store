from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40)
    discount = models.IntegerField()
    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    def get_discount(self):
        return self.price * (1 - self.category.discount / 100)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    
    

    def __str__(self):
        
        return self.name




