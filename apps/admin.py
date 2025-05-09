from django.contrib import admin

from apps.models import DebtBook, ToDo, Category, Product, Card, Order


@admin.register(DebtBook)
class DebtBookAdmin(admin.ModelAdmin):
    list_display = 'id','name','number'


@admin.register(ToDo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','quantity','category_id']

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['id','quantity','product_id']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','status','card_id','user_id']