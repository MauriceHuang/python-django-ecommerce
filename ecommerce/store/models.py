from django.db import models
from django.urls import reverse

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
    
    # def get_absolute_urls(self):
        # return reverse('list-category',args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE, null= True)
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250,default ='unbranded')
    slug = models.SlugField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    description=models.TextField(blank = True)

    class Meta:
        verbose_name_plural ='products'


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product-info',args=[self.slug])