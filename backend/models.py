from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category=models.CharField(max_length=50,null=True,blank=False)
    image = models.ImageField(upload_to="media/products" , null=False,blank=False)

    def __str__(self):
        return self.name




