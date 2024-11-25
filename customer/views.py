from django.shortcuts import render,redirect
from .models import *
from seller .models import *

# Create your views here.
def Home(request):
    return render(request,'customer/Home.html')

# def Login(request): 
#     if request.method == 'POST': 
#         email = request.POST.get('email') 
#         name = request.POST.get('name') 
#         password = request.POST.get('password') 
#         try: 
#             cust = CustomerRegistration.objects.get(email=email, password=password) 
#             request.session['customer'] = cust.id 
#             return redirect('customer:index') 
#         except CustomerRegistration.DoesNotExist: 
#             return render(request, 'customer/Login.html', {'msg': 'Invalid Credentials'}) 
#         except CustomerRegistration.MultipleObjectsReturned: 
#              cust = CustomerRegistration.objects.filter(email=email, password=password).first() # Fallback to use the first entry request.session['customer'] = cust.id return redirect('customer:index') return render(request, 'customer/Login.html'
#              request.session['customer'] = cust.id 
#              return redirect('customer:index') 
#     return render(request, 'customer/Login.html')
def Login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        cust = CustomerRegistration.objects.filter(email=email, password=password).first() # Use filter and get the first entry 
        if cust: 
            request.session['customer'] = cust.id 
            return redirect('customer:index') 
        else: 
            return render(request, 'customer/Login.html', {'msg': 'Invalid Credentials'}) 
    return render(request, 'customer/Login.html')
def SighnUp(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        #create a new user
        customer = CustomerRegistration(name = name, email = email, password = password)
        customer.save()
        return redirect('customer:Login')
    
    return render(request,'customer/SighnUp.html')


def view_category(request, category_name):
    
    category = Category.objects.filter(name=category_name).first()
    
    products = Product.objects.filter(category=category)
    
    context = {
        'category_name': category_name.capitalize(),
        'products': products
    }
    
    return render(request, 'customer/view_products.html',context)


def index(request):
     if 'customer' in request.session:
        return render(request, 'customer/index.html')
    
     else:
        return render(request, 'customer/Home.html')

def productlist(request):
    return render(request,'customer/productlist.html')


def cart(request):
    if 'customer' in request.session:

    # Get all items in the cart
        cart_items = Cart.objects.all()
    
    # Calculate the total price and total quantity
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        total_quantity = sum(item.quantity for item in cart_items)
    
    # Prepare a list to store the total price per item
        total_price_per_item = []
        grand_total = 0
    
    # Loop through the cart items and calculate totals
        for item in cart_items:
            item_total = item.product.price * item.quantity
            total_price_per_item.append({'item': item, 'total': item_total})
            grand_total += item_total

    # Render the cart template with the cart items, totals, and total quantity
        return render(request, 'customer/cart.html', {
            'cart_items': cart_items,
            'grand_total': grand_total,
            'total_price': total_price,
            'total_price_per_item': total_price_per_item,
            'total_quantity': total_quantity  
        })
    
    else:
        return render(request, 'customer/Login.html')



def add_to_cart(request, product_id):
    
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        cart_item, created = Cart.objects.get_or_create( product=product)
        if not created:
                cart_item.quantity += 1
        else:
                cart_item.quantity = 1
                cart_item.save()

    return redirect('customer:cart')


def remove_from_cart(request, product_id):
    cart_item = Cart.objects.get(product_id=product_id)
    cart_item.delete()
    return redirect('customer:cart')



# def search(request):
#      products = None
#      if 'keyword' in request.GET:
#           keyword = request.GET['keyword']
#      if keyword:
#           products = Product.objects.filter(name__icontains=keyword)

#      return render(request,'customer/view_products.html',{'products':products})


def search(request):
    products = None
    if 'keyword' in request.GET:
        keyword = request.GET['keyword'].strip().lower()
        if keyword:
            products = Product.objects.filter(name__icontains=keyword)
    return render(request, 'customer/view_products.html', {'products': products})


def logout(request): # Clear the customer session 
    if 'customer' in request.session: 
        del request.session['customer'] 
    return redirect('customer:Login')

