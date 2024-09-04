from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Product(models.Model):
    PRDName = models.CharField(max_length=100 , verbose_name=_('Product Name'))
    PRDCategory = models.ForeignKey('Category' , on_delete=models.CASCADE , verbose_name=_('Category') ,related_name='category_product')
    
    #from other app
    PRDPrand = models.ForeignKey('settings.Brand',on_delete=models.CASCADE ,verbose_name=_('Brand Name') ,related_name='prand_product',blank=True, null=True)
    # PRDVariant = models.ForeignKey('settings.Variant',on_delete=models.CASCADE ,verbose_name=_('Variant Name') ,related_name='variant_product',blank=True, null=True)
    #---------------
    PRDDescription = models.TextField(max_length=200 , verbose_name=_('Product Description'))
    PRDPrice = models.DecimalField(max_digits=5 , decimal_places=2 , verbose_name=_('Product Price'))
    PRDCost = models.DecimalField(max_digits=5 , decimal_places=2 , verbose_name=_('Product Cost'))
    PRDCreated = models.DateTimeField(verbose_name=_('Created At'))
    PRDImage = models.ImageField(upload_to='product/',blank=True, null=True)
    
    def __str__(self):
        return self.PRDName
    
class Category(models.Model):
    CATName =models.CharField(max_length=50 , verbose_name=_('Category Name'))
    CATParent = models.ForeignKey('self', on_delete=models.CASCADE, limit_choices_to={'CATParent__isnull':True}, blank=True, null=True ,verbose_name=_('Parent Category'))
    CATDescription = models.TextField(verbose_name=_('Description'))
    CATImage = models.ImageField(upload_to='category/',verbose_name=_('Image'))
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
    
    def __str__(self):
        return self.CATName

class ProductImage(models.Model):
    PRDIProduct=models.ForeignKey('Product' , on_delete=models.CASCADE , verbose_name=_('Product Name'))
    PRDIImage = models.ImageField(upload_to='product/' , verbose_name=_('Image'))
    
    def __str__(self):
        return str(self.PRDIProduct)
    

class Product_Alternative(models.Model):
    PALNProduct =  models.ForeignKey('Product',on_delete=models.CASCADE,related_name='main_product', verbose_name=_('Product Name'))
    PALNAlternatives = models.ManyToManyField('Product' ,blank=True,related_name='alternatives_product',verbose_name=_('Alternative'))

    def __str__(self):
        return str(self.PALNProduct)

    class Meta:
        verbose_name = _('Product Alternative')
        verbose_name_plural = _('Product Alternatives')
        
        
class Product_Accessories(models.Model):
    PACCProduct =  models.ForeignKey('Product',on_delete=models.CASCADE,related_name='mainAccessory_product', verbose_name=_('Product Name'))
    PACClternatives = models.ManyToManyField('Product' ,blank=True,related_name='accessories_product' ,verbose_name=_('Accessories'))

    def __str__(self):
        return str(self.PACCProduct)

    class Meta:
        verbose_name = _('Product Accessories')
        verbose_name_plural = _('Product Accessoriess')