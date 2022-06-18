from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product

# Create your views here.
def create(request):
    if request.method == "POST":
        ProductId = request.POST.get('ProductID')
        ProductName = request.POST.get('ProductName')
        data = Product(ProductId=ProductId, ProductName=ProductName)

        data.save()

        return redirect('read')
    else:
        return render(request,'create.html')

def read(request):
    products = Product.objects.all()
    return render(request, 'read.html',{'products':products})

def update(request, pk):
    products = Product.objects.get(id=pk)
    if request.method == "POST":
        return redirect('read')

    context ={
        'products': products,
    }

    return render(request,'update.html', context)
def delete(request, pk):
    products = Product.objects.get(id=pk)

    if request.method == 'POST':
        products.delete()
        return redirect('read')

    context = {
        'products': products,
    }

    return render(request, 'delete.html', context)