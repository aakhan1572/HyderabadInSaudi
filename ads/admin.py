from django.contrib import admin
from ads.models import EVChargingLocation

admin.site.register(EVChargingLocation)


from .models import Photo


@admin.register(Photo)
class PhotoCarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'width', 'height')
    exclude = ('width', 'height')
    list_display_links = ('title', 'timestamp')

    class Meta:
        model = Photo