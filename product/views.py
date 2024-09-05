from django.shortcuts import render
from .models import Product ,ProductImage
from django.core.paginator import Paginator
# Create your views here.


def product_list(request):
    product_list=Product.objects.all()
    paginator=Paginator(product_list,2)
    
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={
        'product_list':page_obj
        }
    
    return render(request,'product/product_list.html',context)


def product_details(request,id):
    product_details=Product.objects.get(id=id)
    product_images=ProductImage.objects.filter(PRDIProduct=id)
    
    paginator=Paginator(product_images,1)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    
    context={
        'product_details':product_details,
        # 'product_images':product_images,
        'product_images':page_obj,
        }
    
    return render(request,'product/product_details.html',context)
