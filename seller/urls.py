from django.urls import path
from . import views
app_name = 'seller'

urlpatterns=[
    path('home/',views.home,name='home'),
    path('Login/',views.Login,name='Login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addproducts/',views.addproducts,name='addproducts'),
    path('viewproducts/',views.viewproducts,name='viewproducts'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
    path('edit_product/<int:id>/', views.edit_product, name='edit_product'),
]