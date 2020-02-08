from django.urls import path
from django.views.decorators.csrf import csrf_exempt

# 3rd party
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# local
from .views import MurrensMethods, murren_register, murren_activate, PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('', MurrensMethods.as_view(), name='MurrensMethods'),

    # rest
    path('register/', csrf_exempt(murren_register), name='murren_register'),
    path('activation/', csrf_exempt(murren_activate), name='murren_activate'),

    # reset
    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/confirm/', PasswordResetConfirmView.as_view(), name='password_confirm'),

    # 3rd party
    path('token_create/', TokenObtainPairView.as_view(), name='obtain_token_pair'),
    path('token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
