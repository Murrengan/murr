from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Murren.views import count_murren, landing, profile, redirect_view
from murr import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('profile/', profile, name='profile'),
    path('count_murren/', count_murren, name='count_murren'),
    path('murrs/', include('Murr_card.urls')),
    path('murren/', include('Murren.urls')),
    path('landing/', landing, name='landing'),
    path('', redirect_view, name='redirect_view'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
