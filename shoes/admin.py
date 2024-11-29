from django.contrib import admin
from .models import Shoes
from .models import Brand

class ShoesAdmin(admin.ModelAdmin):
    list_filter = ("brand", "name", "price")
    list_display = ("name", "brand", "price", "in_stock")

# Register your models here.
admin.site.register(Shoes, ShoesAdmin)
admin.site.register(Brand)