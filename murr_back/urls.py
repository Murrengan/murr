from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),

    # 3rd party
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),

    # local
    path('murren/', include('murren.urls')),
    path('murr_card/', include('murr_card.urls')),


]
