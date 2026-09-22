from django.shortcuts import render

from .models import Product, Category

def product_list(request):
    categories = Category.objects.all()

    category_id = request.GET.get('category')

    
    search = request.GET.get('q')
    if search:
        products = Product.objects.filter(name__icontains=search)
    elif category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    return render(request, 'shop/product_list.html', {'products': products, 'categories': categories})

def product_more(request, pk):
    details = Product.objects.get(pk=pk)
    return render(request, 'shop/product_info.html', {'details': details})