from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from Murren import views

urlpatterns = [
    path('', views.redirect_view, name='redirect_view'),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('edit/', views.murren_edit, name='edit'),
    path('murrs/', include('Murr_card.urls')),
    path('landing/', views.landing, name='landing'),
    path('', include('Murren.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
