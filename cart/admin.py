from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ['user','product', 'variation','quantity']
    search_fields = ['product']
    search_fields = ['user__first_name']



admin.site.register(Cart,CartAdmin)
