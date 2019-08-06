from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Murren import views as murren
from .views import redirect_view, about

urlpatterns = [
    path('', redirect_view, name='redirect_view'),
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('edit/', murren.murren_edit, name='edit'),
    path('murrs/', include('MurrCard.urls')),
    path('landing/', murren.landing, name='landing'),
    path('murren/', include('Murren.urls')),
    path('dashboard/', include('Dashboard.urls')),
    path('murr_game/', include('murr_game.urls')),
    path('murr_ui/', include('murr_ui.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
