from django.db import models

# Create your models here.

class tags(models.Model):
    tag_name = models.CharField(max_length=20,null=True,blank=False,default='')
    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

class Product(models.Model):
    product_code = models.CharField(max_length=10,null=True,blank=False,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    product_category = models.CharField(max_length=15,null=True,blank=False)
    product_type = models.CharField(max_length=15,null=True,blank=False)
    tag = models.ManyToManyField(tags,related_name='product_tags',blank=True)

    def __str__(self):
        return self.product_code+ " / "+self.product_category+" "+self.product_type
        
class MetalDetails(models.Model):
    product = models.ForeignKey(Product,null=True,blank=False,related_name='metal_details')

    metal_choices = (('Yellow Gold','Yellow Gold'),('White Gold','White Gold'))
    metal = models.CharField(max_length=15,choices=metal_choices,null=True,blank=False,unique=True)
    carat_choices=(('14','14'),('16','16'),('18','18'),('19','19'),('20','20'),('21','21'),('22','22'),('23','23'),('24','24'))
    carats=models.CharField(max_length=2,choices=carat_choices,null=True,blank=False,unique=True)

    weight_of_metal = models.DecimalField(max_digits=8,decimal_places=5,null=True,blank=False)
    price_for_metal = models.IntegerField(blank=False,null=True)
    making_charges = models.IntegerField(blank=False,null=True)

    def __str__(self):
        return self.metal +" "+self.carats+"kt"

    class Meta:
        verbose_name_plural = "Metal Detail"
        verbose_name_plural = "Metal Details"

class DiamondDetails(models.Model):
    product = models.ForeignKey(Product,null=True,blank=False,related_name='diamond_details')

    clarity_choices = (('FL','FL'),('IF','IF'),('VVS1','VVS1'),('VVS2','VVS2'),('SI1','SI1'),('SI2','SI2'),('I1','I1'),('I2','I2'),('I3','I3'))
    diamond_clarity = models.CharField(max_length=4,choices=clarity_choices,blank=True,null=True,unique=True)
    color_choices = (('DF','DF'),('GH','GH'),('IJ','IJ'),('KM','KM'),('NR','NR'),('SZ','SZ'))
    diamond_color = models.CharField(max_length=2,choices=color_choices,default='',null=True,blank=True)
    shape_choices = (('Other','Other'),('Round','Round'),('Oval','Oval'),('Pear','Pear'),('Heart','Heart'),('Princess','Princess'),('Asscher','Asscher'),('Marquise','Marquise'),('Emerald','Emerald'),('Radiant','Radiant'),('Cushion','Cushion'))
    diamond_shape = models.CharField(max_length=15,choices=shape_choices,blank=True,null=True)

    number_of_diamonds=models.IntegerField(null=True,blank=False)
    weight_of_diamonds=models.DecimalField(max_digits=8,decimal_places=5,null=True,blank=False)
    diamond_price=models.IntegerField()

    def __str__(self):
        return self.diamond_clarity+" / "+self.diamond_color+" / "+self.diamond_shape

    class Meta:
        verbose_name = "Diamond Detail"
        verbose_name_plural = "Diamond Details"

class GemstoneDetails(models.Model):
    product = models.ForeignKey(Product,null=True,blank=False,related_name='gemstone_details')

    gemstone = models.CharField(max_length=15,blank=False,null=True)
    shape_choices = (('Other','Other'),('Round','Round'),('Oval','Oval'),('Pear','Pear'),('Heart','Heart'),('Princess','Princess'),('Asscher','Asscher'),('Marquise','Marquise'),('Emerald','Emerald'),('Radiant','Radiant'),('Cushion','Cushion'))

    gemstone_shape = models.CharField(max_length=15,choices=shape_choices,blank=True,null=True)
    number_of_gemstones=models.IntegerField(null=True,blank=False)
    weight_of_gemstones=models.DecimalField(max_digits=8,decimal_places=5,null=True)#---------------------------Currently not included in admin site
    gemstone_price=models.IntegerField(null=True,blank=False)
