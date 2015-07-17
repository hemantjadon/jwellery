from django.db import models
from register.models import MyUser
from Products.models import *
# Create your models here.
class orderDeliveryDetails(models.Model):
	phone = models.CharField(max_length=12,default='') 
    street_address = models.CharField(max_length = 100, null=True, blank=True)
    city = models.CharField(max_length=20,blank=True, null=True)
    pincode = models.CharField(max_length=8, default="0000000")


class order(models.Model):
	user=models.ForeignKey(MyUser)
	orderId=models.CharField(max_length=15) #create using datetime+userid+productCode at the time of placing order is updated
	orderPlacedDate=models.DateTimeField([auto_now=True)
    earingProduct=models.ForeignKey(earingProduct)
    bangleProduct=models.ForeignKey(bangleProduct,default='',blank=True)
    ringProduct=models.ForeignKey(ringProduct,default='',blank=True)
    braceletProduct=models.ForeignKey(braceletProduct,default='',blank=True)
    nosepinProduct=models.ForeignKey(nosepinProduct,default='',blank=True)
    necklaceProduct=models.ForeignKey(necklaceProduct,default='',blank=True)
    managalsutraProduct=models.ForeignKey(mangalsutraProduct,default='',blank=True)
    deliveryDate=models.DateField()
    orderDelivered=models.BooleanField(default=False)
    orderCancelled=models.BooleanField(default=False)
    isBasicAddress=models.BooleanField(default=True)
    isNotBasicAddress=models.ForeignKey(orderDeliveryDetails,blank=True,null=True)
    orderAmount=models.IntegerField()

    def __str__(self):
        return self.orderId




