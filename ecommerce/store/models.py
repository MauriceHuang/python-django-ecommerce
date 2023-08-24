from django.db import models

# Create your models here.

#categories modal 

class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)

    slug = models.SlugField(max_length=20,unique= True)

    class Meta:
# the actually alter the pural name since category"s" is not the accurate representation of pural form of category.
        verbose_name_plural = 'categories'

# by default, the Category will be in numeral, to alter the default behaviour to use the name instead, will be as below

    def __str__ (self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250,default ='unbranded')
    slug = models.SlugField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description=models.TextField(blank = True)

    class Meta:
        verbose_name_plural ='products'


    def __str__(self):
        return self.title
