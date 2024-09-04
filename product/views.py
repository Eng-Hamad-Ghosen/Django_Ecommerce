from django.shortcuts import render
from .models import Product ,ProductImage
# Create your views here.


def product_list(request):
    product_list=Product.objects.all()
    context={
        'product_list':product_list
        }
    
    return render(request,'product/product_list.html',context)


def product_details(request,id):
    product_details=Product.objects.get(id=id)
    product_images=ProductImage.objects.filter(PRDIProduct=id)
    context={
        'product_details':product_details,
        'product_images':product_images
        }
    
    return render(request,'product/product_details.html',context)
