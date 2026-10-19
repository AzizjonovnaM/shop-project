from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField("Name category:",max_length=100)
    description=models.TextField("Opisanie:",blank=True)

    class Meta:
        verbose_name="CATEGORY"
        verbose_name_plural="CATEGORIES"

    def __str__(self):
        return self.name 


class Product(models.Model):
    name=models.CharField("Nazvanie tovara:",max_length=100)
    price=models.DecimalField("Sena:",max_digits=10, decimal_places=2)
    size=models.CharField("Razmer:",max_length=20)
    color=models.CharField("Svet:",max_length=50)
    quantity=models.PositiveIntegerField("Kolichestvo:",default=0)
    category=models.ForeignKey("shop.Category",on_delete=models.CASCADE,related_name="products")

    class Meta:
        verbose_name="PRODUCT"
        verbose_name_plural="PRODUCTS"

    def __str__(self):
        return self.name 

class Order(models.Model):
    customer_name=models.CharField("Imya pokupatelya:",max_length=100)
    product=models.ForeignKey("shop.Product",on_delete=models.CASCADE,related_name="orders")
    quantity=models.PositiveIntegerField("Kolichestvo:",default=1)
    order_date=models.DateTimeField("Data zakaza:",auto_now_add=True)
    status=models.CharField("Status:",max_length=30,default="New")

    class Meta:
        verbose_name="ORDER"
        verbose_name_plural="ORDERS"

    def __str__(self):
        return f"Zakaz N:{self.id}-{self.customer_name}"
                        