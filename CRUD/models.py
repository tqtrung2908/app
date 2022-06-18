from django.db import models

class Product(models.Model):
    ProductID = models.CharField(max_length=10)
    ProductName = models.CharField(max_length=100)
    #ProductImage = models.ImageField(upload_to=None)
    class Meta:
        db_table ="Product"
