from django.shortcuts import render,redirect
from .models import products  # class name products
from .forms import ProductForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def ShowAllProducts(request):
    product1=products.objects.all()
    page_num=request.GET.get('page')
    paginator=Paginator(product1,3)
    try:
        product1=paginator.page(page_num)
    except PageNotAnInteger:
        product1=paginator.page(1)
    except EmptyPage:
        product1=paginator.page(paginator.num_pages)
    
    number_of_products=products.objects.all().count()
    print("Total No Of Records in the Table is:",number_of_products)
    
    context={
        "product1":product1
        
    }
    
    return render(request,"showproducts.html",context)


def ProductDetails(request,pk):
    EachProduct=products.objects.get(id=pk)# select * from tablename  where id=1
    context={
        "EachProduct":EachProduct
    }
    return render(request,'productDetails.html',context)
    

def AddProducts(request):
    form=ProductForm()
    if request.method=='POST':#post==post=>True
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showproducts')
        
    context={
        'form':form,
    }
    return render(request,"addproducts.html",context)


def UpdateProduct(request,pk):
    product1=products.objects.get(id=pk)
    form=ProductForm(instance=product1)
    if request.method=='POST': # post==post =>true
        form=ProductForm(request.POST,request.FILES,instance=product1)
        if form.is_valid():
            form.save()
            return redirect('showproducts')
    context={
        'form':form
    }
    return render(request,"updateproduct.html",context)


def deleteProduct(request,pk):
    product=products.objects.get(id=pk)
    product.delete()
    return redirect('showproducts')
    
        
    

def searchBar(request):
    if request.method=="GET":     #get==get
        query=request.GET.get('query')
        if query:
            product=products.objects.filter(name__icontains=query)
            return render(request,'searchBar.html',{'productInfo':product})
        else:
            print("No Products Found")
            return render(request,'searchbar.html',{})
    
