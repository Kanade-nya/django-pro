from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Character,GoodsIP,Goods

admin.site.register(Character)
admin.site.register(GoodsIP)
admin.site.register(Goods)