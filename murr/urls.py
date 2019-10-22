from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Murren import views as murren
from .views import about

urlpatterns = [
    path('', about, name='about'),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('edit/', murren.murren_edit, name='edit'),
    path('murrs/', include('MurrCard.urls')),
    path('landing/', murren.landing, name='landing'),
    path('murren/', include('Murren.urls')),
    path('murr_game/', include('murr_game.urls')),

    # api
    path('api_auth/', include('rest_framework.urls')),
    path('murr_api/', include('murr_api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
