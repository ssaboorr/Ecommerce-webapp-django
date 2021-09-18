from django.contrib import admin
from .models import Customer, Product, OrderPlaced, Cart


# Register your models here.

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'city', 'zip_address']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'sub_category']


@admin.register(OrderPlaced)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'order_date']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']
