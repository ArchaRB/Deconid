from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def home(request):
    return render(request,'seller/home.html')

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if SellerRegistration.objects.filter(email = email, password = password).exists():
            return redirect('seller:dashboard')
        else:
            return render(request, 'seller/Login.html',{'msg':'Invalid email or password'})

    return render(request,'seller/Login.html')

def addproducts(request):
    categories = Category.objects.all()  # Fetch all categories
    
    if request.method == 'POST':
        name = request.POST.get('productname')  # Match form field name
        price = request.POST.get('productprice')  # Match form field name
        description = request.POST.get('productdescription')  # Match form field name
        category1 = request.POST.get('productcategory')  # Match form field name
        image = request.FILES.get('productimage')  # Match form field name
        
        # Print the category1 value to debug
        print(f"Category ID from form: {category1}")

        try:
            # Get the category object by id
            cat = Category.objects.get(id=category1)
            # Save the new product
            Product(name=name, price=price, description=description, category=cat, image=image).save()
            msg = 'Product added successfully!'
        except Category.DoesNotExist:
            msg = 'Selected category does not exist.'
        
        return render(request, 'seller/addproducts.html', {'categories': categories, 'msg': msg})
    
    # Render the dashboard with the categories context
    return render(request, 'seller/addproducts.html', {'categories':categories})
                                                       
def viewproducts(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'seller/viewproducts.html', {'products':products})

def dashboard(request):
    return render(request,'seller/dashboard.html')



from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    categories = Category.objects.all()
    
    if request.method == 'POST':
        product.name = request.POST.get('productname')
        product.description = request.POST.get('productdescription')
        category_id = request.POST.get('productcategory')

        print(f"Submitted Category ID: {category_id}")

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return redirect('seller:viewproducts')  # Redirect to the view products page to see the updates
                
        product.category = category
        product.price = request.POST.get('productprice')

        if 'productimage' in request.FILES:
            product.image = request.FILES['productimage']

        product.save()

        return render(request, 'seller/edit_product.html', {
            'product': product,
            'categories': categories,
            'msg': 'Product updated successfully!'
        })
    
    return render(request, 'seller/edit_product.html', {
        'product': product,
        'categories': categories
    })


def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('seller:viewproducts')
