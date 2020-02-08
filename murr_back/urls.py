from django.contrib import admin
from django.urls import path, include, re_path

from murren.views import PasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),

    # 3rd party
    path('api-auth/', include('rest_framework.urls')),

    # local
    path('murren/', include('murren.urls')),
    path('murr_card/', include('murr_card.urls')),
    re_path(r'^confirm-password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            PasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),

]
