from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Brand(models.Model):
    PRDName = models.CharField(max_length=50 ,verbose_name=_('Brand Name'))
    PRDDescription = models.TextField(verbose_name=_('Brand Description'), blank=True, null=True)

    def __str__(self):
        return self.PRDName

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        
        
class Variant(models.Model):
    VARName = models.CharField(max_length=50 ,verbose_name=_('Variant Name'))
    VARDescription = models.TextField(verbose_name=_('Variant Description') ,blank=True, null=True)

    def __str__(self):
        return self.VARName
    
    class Meta:
        verbose_name = 'Variant'
        verbose_name_plural = 'Variants'