from django.contrib import admin
from .models import*




class WebsiteSettingAdmin(admin.ModelAdmin):
    list_display = ['title','email','mobile']

admin.site.register(WebsiteSetting,WebsiteSettingAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = ['heading', 'sub_heading', 'image', 'status']
    list_filter = ['heading']
    search_fields = ['heading']


admin.site.register(Slider,SliderAdmin)

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ['title'] }
    list_display = ['title','date_time','status']
    list_filter = ['title']
    search_fields = ['title']


admin.site.register(Blog,BlogAdmin)


class FAQAdmin(admin.ModelAdmin):
    list_display = ['question']
    list_filter = ['question']
    search_fields = ['question']

admin.site.register(FAQ,FAQAdmin)
