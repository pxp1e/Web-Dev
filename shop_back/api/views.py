from django.http import JsonResponse
from .models import Product, Category

def products_list(request):
    products = Product.objects.all().values()
    return JsonResponse(list(products), safe=False)

def product_detail(request, id):
    product = Product.objects.filter(id=id).values().first()
    return JsonResponse(product, safe=False)

def categories_list(request):
    categories = Category.objects.all().values()
    return JsonResponse(list(categories), safe=False)

def category_detail(request, id):
    category = Category.objects.filter(id=id).values().first()
    return JsonResponse(category, safe=False)

def category_products(request, id):
    products = Product.objects.filter(category_id=id).values()
    return JsonResponse(list(products), safe=False)