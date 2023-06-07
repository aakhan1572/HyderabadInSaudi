from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.bbglist,name='bbglist'),
    path('bbgads/', views.bbgads, name='bbgads'),
    path('bbgads/<int:id>/', views.bbgdetail, name='bbgdetail'),
    
]

#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 