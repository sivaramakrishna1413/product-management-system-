from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from product import views

urlpatterns=[
    # path('admin/',admin.site.urls),
    path('',views.ShowAllProducts,name="showproducts"),
    path('oneproduct/<int:pk>/',views.ProductDetails,name="productDetails"),
    path('addproduct/',views.AddProducts,name='addProduct'),
    path('UpdateProduct/<int:pk>/',views.UpdateProduct,name="updateproduct"),
    path('deleteproduct/<int:pk>/',views.deleteProduct,name="DeleteProduct"),
    path('Searchproduct/',views.searchBar,name='search'),
    path('Category',views.ShowAllProducts,name='category')
    
    ]

#  ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
