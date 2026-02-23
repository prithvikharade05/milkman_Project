from django.contrib import admin
from .models import Customer, Category, Product, Subscription

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Subscription)