from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from Murren.views import count_murren, signup, landing, profile
from murr import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='Murren/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),


    path('tinymce/', include('tinymce.urls')),

    path('', count_murren, name='count_murren'),

    path('murrs/', include('Murr_card.urls')),
    path('landing/', landing, name='landing'),



    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
