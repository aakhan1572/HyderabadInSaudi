import os
from django.db import models
from accounts.models import User
from expads.models import Category,Countrycode,CityCode
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from sorl.thumbnail import get_thumbnail
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField



class Bbgproject(models.Model):
    user = models.ForeignKey(User ,  on_delete=models.CASCADE)
    category = models.ForeignKey(Category ,  on_delete=models.CASCADE)
    fullname = models.CharField(max_length=150)
    countrycode = models.ForeignKey(Countrycode ,default='Saudi Arabia',  on_delete=models.CASCADE)
    citycode = models.ForeignKey(CityCode ,  default='Jeddah',on_delete=models.CASCADE)
    locationcode =models.CharField(max_length=200)
    sublocationcode = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    Description = models.CharField(max_length=500)
    contactno = PhoneNumberField()
    is_active = models.BooleanField(default=True)
    cover_photo = models.FileField(upload_to='users/bbgcover_photos', blank=True, null=True)    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created','-updated')
        verbose_name = 'bbgproject'
        verbose_name_plural = 'bbgprojects'

    def __str__(self):
        return self.fullname


class BbgImage(models.Model):
    bbgprojects = models.ForeignKey(Bbgproject, on_delete=models.CASCADE,related_name='bbgproject')
    images = models.FileField(upload_to='users/bbgimages', blank=True, null=True)

    @property
    def thumbnail(self):
        if self.images:
            return get_thumbnail(self.images, '50x50', quality=90)
        return None
    
    def __str__(self):
        return self.bbgprojects.fullname     



@receiver(models.signals.post_delete, sender=Bbgproject)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.cover_photo.delete(save=False)

@receiver(models.signals.post_delete, sender=BbgImage)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.images.delete(save=False)
