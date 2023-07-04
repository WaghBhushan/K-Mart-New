from django.contrib import admin, messages
from .models import*


class OrderDetailsInline(admin.TabularInline):
    model = OrderDetails


def active_status(modelAdmin,request,queryset):
    try:
        queryset.update(payment=True)
        messages.success(request,'selected record(s) mark as active')
    except Exception as e:
        messages.error(request, str(e)) 

def inActive_status(modelAdmin,request,queryset):
    try:
        queryset.update(payment= False)
        messages.success(request,'selected record(s) mark as active')
    except Exception as e:
        messages.error(request, str(e)) 

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','mobile','payment','status']
    search_fields = ['id','user__first_name']
    list_filter = ['status', 'payment']
    inlines = (OrderDetailsInline, )
admin.site.register(Order,OrderAdmin)


