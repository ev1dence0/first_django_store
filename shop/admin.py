from django.contrib import admin

from .models import Product, Category



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'get_discount')
    search_fields = ('name',)
    list_filter = ('category',)
    ordering = ('price',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
    