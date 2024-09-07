from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
# Create your models here.
def upload_image(instance,filename):
    image_name,extention=filename.split('.')
    return 'accounts/%s/%s.%s'%('profile/',instance.user.username,extention)

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE ,related_name='user_profile' ,verbose_name=_('Username'))
    mobile= models.CharField(max_length=15 ,verbose_name=_('Mobile'))
    image=models.ImageField(upload_to=upload_image ,verbose_name=_('Image') ,blank=True, null=True)
    citty=CountryField()
    def __str__(self):
        return str(self.user)#OR return "%s" %(self.user)
        

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

@receiver(post_save,sender=User)
def auto_create_profile(sender,instance ,created ,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        
# or 

# def auto_create_profile(sender,**kwargs):
#     if kwargs['created']:
#         Profile.objects.create(user=kwargs['instance'])
# post_save.connect(auto_create_profile,sender=User)