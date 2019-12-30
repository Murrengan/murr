from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # 3rd party
    path('api-auth/', include('rest_framework.urls')),

    # local
    path('murren/', include('murren.urls')),
    path('murr_card/', include('murr_card.urls')),

]
