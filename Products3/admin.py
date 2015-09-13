from django.contrib import admin
from django import forms
from Products3.models import *

# Register your models here.

class MetalDetailsInline(admin.TabularInline):
    model = MetalDetails
    min_num = 1
    extra = 0
    fields = ['carats','metal','weight_of_metal','price_for_metal','making_charges']


class DiamondDetailsInline(admin.TabularInline):
    model = DiamondDetails
    extra = 1
    fields=['diamond_clarity','diamond_color','diamond_shape','number_of_diamonds','weight_of_diamonds','diamond_price']

class GemstoneDetailsInline(admin.TabularInline):
    model = GemstoneDetails
    extra = 1
    fields = ['gemstone','gemstone_shape','number_of_gemstones','gemstone_price']

class ProductAdmin(admin.ModelAdmin):
    fields = (('product_code','product_category','product_type'),'tag')
    inlines = (MetalDetailsInline,DiamondDetailsInline,GemstoneDetailsInline)

admin.site.register(tags)
admin.site.register(Product,ProductAdmin)