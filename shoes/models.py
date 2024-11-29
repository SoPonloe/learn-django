from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Shoes(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return f"\n {self.brand} {self.name} ({self.price}) {self.in_stock} \n"