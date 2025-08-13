from django.shortcuts import render,redirect
from .services import Shopee
from django.contrib import messages
from django.views.decorators.cache import never_cache

def index(request):
    return render(request, "index.html")


def products(request):
    return render(request, "add_product.html")


def add_product_view(request):
    if request.method == "POST":
        category_id = request.POST.get("category_id")
        product_name = request.POST.get("product_name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        stock_quantity = request.POST.get("stock_quantity")
        image_url = request.POST.get("image_url")
        is_featured = request.POST.get("is_featured") or 0

        service = Shopee()

        try:
            service.add_product(
                category_id, product_name, description,
                price, stock_quantity, image_url, is_featured
            )
            messages.success(request, "Product added successfully!")
            return redirect("add_product")
        except Exception as e:
            messages.error(request, f"Error adding product: {e}")

    return render(request, "add_product.html")

def category_list(request):
    obj = Shopee()
    categories = obj.show_category()
    return render(request, 'category_list.html', {'categories': categories})

def product_list(request):
    obj = Shopee()
    product = obj.show_product()
    return render(request,'product_list.html', {'product':product})



def delete_product_by_id(request):
    obj = Shopee()
    if request.method == "POST":
        product_id = int(request.POST.get("product_id"))
        # Try to delete
        deleted = obj.delete_product(product_id)        
        if deleted:
            messages.success(request, f"Product with ID {product_id} deleted successfully.")
        else:
            messages.error(request, "Product not found.")

    return render(request, 'delete_product.html')



