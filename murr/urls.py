from django.contrib import admin
from django.urls import path, include

from Murren.views import home, signup

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('', home, name='home')
]
