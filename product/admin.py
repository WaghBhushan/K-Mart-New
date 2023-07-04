from django.contrib import admin,messages
from . models import*


def active_status(modelAdmin,request,queryset):
    try:
        queryset.update(status=True)
        messages.success(request,'selected record(s) mark as active')
    except Exception as e:
        messages.error(request, str(e)) 

def inActive_status(modelAdmin,request,queryset):
    try:
        queryset.update(status= False)
        messages.success(request,'selected record(s) mark as active')
    except Exception as e:
        messages.error(request, str(e)) 
    


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','status','show_on_homepage']
    list_filter = ['name']
    search_fields = ['name']

admin.site.register( ProductCategory,ProductCategoryAdmin)






def active_status(modelAdmin,request,queryset):
    try:
        queryset.update(status=True)
        messages.success(request,'selected record(s) mark as active')
    except Exception as e:
        messages.error(request, str(e)) 

def inActive_status(modelAdmin,request,queryset):
    try:
        queryset.update(status= False)
        messages.success(request,'selected record(s) mark as active')
    except Exception as e:
        messages.error(request, str(e)) 


class ProductVariationAdmin(admin.ModelAdmin):
    list_display = ['name','status']
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(ProductVariation,ProductVariationAdmin)




def active_status(modelAdmin,request,queryset):
    try:
        queryset.update(status=True)
        messages.success(request,'selected record(s) mark as active')
    except Exception as e:
        messages.error(request, str(e)) 

def inActive_status(modelAdmin,request,queryset):
    try:
        queryset.update(status= False)
        messages.success(request,'selected record(s) mark as active')
    except Exception as e:
        messages.error(request, str(e)) 

class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['name','status']
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(ProductTag,ProductTagAdmin)









def active_status(modelAdmin,request,queryset):
    try:
        queryset.update(status=True)
        messages.success(request,'selected record(s) mark as active')
    except Exception as e:
        messages.error(request, str(e)) 

def inActive_status(modelAdmin,request,queryset):
    try:
        queryset.update(status= False)
        messages.success(request,'selected record(s) mark as active')
    except Exception as e:
        messages.error(request, str(e)) 


class ProductImagesInline(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' :('name', )}
    list_display = ['name','price','product_category','status']
    list_filter = ["product_category"]
    search_fields = ['name']
    inlines = (ProductImagesInline, ) 
    actions = (active_status,inActive_status)

admin.site.register(Product,ProductAdmin)


