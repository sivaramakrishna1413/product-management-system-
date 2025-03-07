from django.contrib import admin
from product.models import products,Category

# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display=('id','name','price','is_publish','created_at')
    list_display_links=('price','name')
    list_filter=('price','created_at')
    list_editable=('is_publish',)
    search_fields=('name','id')
    ordering=('price',)#ordering the data according to req by low to high by deafault
    exclude=('description',)
    
admin.site.register(products,productAdmin)
admin.site.register(Category)


