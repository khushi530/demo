from django.contrib import admin
from app1.models import *

class userdisp(admin.ModelAdmin):
    list_display=['username','email','phone']
    list_filter=['username','email','phone']
    search_fields=['username','email','phone']
admin.site.register(User,userdisp)
admin.site.register(Category)
admin.site.register(Product)
# Register your models here.
