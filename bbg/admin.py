from django.contrib import admin

from .models import Bbgproject,BbgImage


class BbgprojectAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'countrycode','citycode','locationcode','sublocationcode', 'landmark','contactno','price','Description','is_active','cover_photo')
admin.site.register(Bbgproject, BbgprojectAdmin)

class BbgImageAdmin(admin.ModelAdmin):
    list_display = ('bbgprojects', 'images')
admin.site.register(BbgImage, BbgImageAdmin)