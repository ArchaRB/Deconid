from django.urls import path
from .import views
app_name='customer'


urlpatterns = [
    path('',views.Home,name='Home'),
    path('SighnUp/',views.SighnUp,name='SighnUp'),
    path('Login/',views.Login,name='Login'),
    path('index/',views.index,name='index'),
    path('productlist/',views.productlist,name='productlist'),
    path('view_category/<str:category_name>/', views.view_category, name='view_category'),
    path('view_products/<str:category_name>/', views.view_category, name='view_products'), 
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart,name='cart'),
    path('remove_from_cart/<int:product_id>/',views.remove_from_cart,name='remove_from_cart'),
    path('search/',views.search,name='search'),
    path('logout/', views.logout, name='logout'),    
    ]

