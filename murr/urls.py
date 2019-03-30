from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Murren.views import count_murren, signup, landing
from murr import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tinymce/', include('tinymce.urls')),

    path('', count_murren, name='count_murren'),
    path('signup/', signup, name='signup'),
    path('murrs/', include('Murr_card.urls')),

    path('landing/', landing, name='landing'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
