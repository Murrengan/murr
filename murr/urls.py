from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Murren import views as murren

urlpatterns = [
    path('', murren.redirect_view, name='redirect_view'),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('edit/', murren.murren_edit, name='edit'),
    path('murrs/', include('Murr_card.urls')),
    path('landing/', murren.landing, name='landing'),
    path('murren/', include('Murren.urls')),
    path('<str:username>/', murren.profile, name='murren_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
