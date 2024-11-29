from django.shortcuts import render
from .models import Shoes

# Create your views here.

def index(request):
    shoes =  Shoes.objects.all()
    total_shoes = shoes.count()
    return render(request, "shoes/shoe_detail.html", {
        "shoes": shoes, 
        "total_shoes": total_shoes
    })