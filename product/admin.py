from django.contrib import admin
from product.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname','productdesc','producter','create_time','id']

admin.site.register(Product,ProductAdmin)