from django.contrib import admin
from django import forms
from django.db import models
from Products.models import *
from django.forms import CheckboxSelectMultiple
from django.apps import apps

# Register your models here.
#------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Form For Admin Site------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------#

class ProductForm(forms.ModelForm):
	def clean_productCode(self):#------------------------------------------Cleaning Product code for uniqueness of object#
		print("yeahh")
		productCode=self.cleaned_data['productCode']
		products=[]
		app=apps.get_app_config('Products')
		models=app.models.values()
		for model in models:
			flag=True
			fields=model._meta.get_all_field_names()
			for field in fields:
				if field=='productCode':
					products+=model.objects.filter(productCode=productCode)
					if model.objects.filter(productCode=productCode):
						flag=False
						break
			if not flag:
				print(products)
				break
		if(len(products) is not 0):
			self._errors['productCode']=self.error_class(["Product with this Product Code already exists"])
			raise forms.ValidationError("")
		else:
			return self.cleaned_data['productCode']


#-------------------------------------------------------X-X-X------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------Inline Models----------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------#

class metalDetailsInline(admin.TabularInline):
	model=metalDetails
	min_num=1
	extra = 0
	fields=['carats','metal','weightOfMetal','priceForMetal']
	filter_horizontal_checkbox = ('carats',)
	formfield_overrides = {models.ManyToManyField: {'widget': CheckboxSelectMultiple}}

class diamondDetailsInline(admin.TabularInline):
    model = diamondDetails
    extra = 1
    fields=['diamond','diamondColor','diamondShape','numberOfDiamonds','weightOfDiamonds','diamondPrice']

class gemstoneDetailInline(admin.TabularInline):
    model = gemstoneDetails
    extra = 1
    fields=['gemstone','gemstoneShape','numberOfGemstones','gemstonePrice']


#-------------------------------------------------------X-X-X------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------Admin Product View------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------#

class EaringProductAdmin(admin.ModelAdmin):
	form = ProductForm
	fields=(('productCode','productType'),'makingCharges','tag')
	inlines=(metalDetailsInline,diamondDetailsInline,gemstoneDetailInline)

class BangleProductAdmin(admin.ModelAdmin):
	form=ProductForm
	fields=(('productCode','productType'),'makingCharges','tag')
	inlines=(metalDetailsInline,diamondDetailsInline,gemstoneDetailInline)

class RingProductAdmin(admin.ModelAdmin):
	form=ProductForm
	fields=(('productCode','productType'),'makingCharges','tag')
	inlines=(metalDetailsInline,diamondDetailsInline,gemstoneDetailInline)

class BraceletProductAdmin(admin.ModelAdmin):
	form=ProductForm
	fields=(('productCode','productType'),'makingCharges','tag')
	inlines=(metalDetailsInline,diamondDetailsInline,gemstoneDetailInline)

class NosepinProductAdmin(admin.ModelAdmin):
	form=ProductForm
	fields=(('productCode','productType'),'makingCharges','tag')
	inlines=(metalDetailsInline,diamondDetailsInline,gemstoneDetailInline)

class NecklaceProductAdmin(admin.ModelAdmin):
	form=ProductForm
	fields=(('productCode','productType'),'makingCharges','tag')
	inlines=(metalDetailsInline,diamondDetailsInline,gemstoneDetailInline)

class MangalsutraProductAdmin(admin.ModelAdmin):
	form=ProductForm
	fields=(('productCode','productType'),'makingCharges','tag')
	inlines=(metalDetailsInline,diamondDetailsInline,gemstoneDetailInline)


#-------------------------------------------------------X-X-X------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------Registering-------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------#

#admin.site.register(DIAMOND)
#admin.site.register(GEMSTONES)
#admin.site.register(METAL)
#admin.site.register(METALCARAT)
#admin.site.register(tags)
admin.site.register(earingProduct,EaringProductAdmin)
admin.site.register(bangleProduct,BangleProductAdmin)
admin.site.register(ringProduct,RingProductAdmin)
admin.site.register(braceletProduct,BraceletProductAdmin)
admin.site.register(nosepinProduct,NosepinProductAdmin)
admin.site.register(necklaceProduct,NecklaceProductAdmin)
admin.site.register(mangalsutraProduct,MangalsutraProductAdmin)

#-------------------------------------------------------X-X-X------------------------------------------------------------#