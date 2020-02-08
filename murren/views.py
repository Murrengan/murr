from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import json

# 3rd party
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# local
from .forms import MurrenSignupForm
from .serializers import PasswordResetSerializer, PasswordResetConfirmSerializer

Murren = get_user_model()


class MurrensMethods(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        r = Murren.objects.get(id=request.user.id)
        data = {'murren_name': r.username}
        return Response(data)


def murren_register(request):

    if request.method == 'POST':

        json_data = json.loads(request.body)

        murren_data = {

            'username': json_data['username'],
            'email': json_data['email'],
            'password': json_data['password']
        }

        form = MurrenSignupForm(murren_data)

        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = False
            user.set_password(murren_data.get('password'))
            user.save()

            message = 'http://127.0.0.1:8080' + '/murren_email_activate/?activation_code=' \
                      + urlsafe_base64_encode(force_bytes(user.pk))
            subject = 'Активация аккаунта Муррена'
            email = EmailMessage(subject, message, to=[murren_data.get('email')])
            email.send()

            return JsonResponse({'is_murren_created': 'true'}, status=status.HTTP_201_CREATED)

        else:

            return JsonResponse(form.errors)


def murren_activate(request):

    if request.method == 'POST':

        try:

            json_data = json.loads(request.body)
            murren_id = force_text(urlsafe_base64_decode(json_data['murren_id']))
            murren = Murren.objects.get(pk=murren_id)

        except(TypeError, ValueError, OverflowError, Murren.DoesNotExist) as error:

            murren = None

        if murren is not None:

            murren.is_active = True
            murren.save()

            return HttpResponse("User is active now")

        else:

            return HttpResponse('Activation link is invalid!')


class PasswordResetView(generics.CreateAPIView):
    """End Point reset password"""
    serializer_class = PasswordResetSerializer
    permission_classes = (AllowAny,)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.serializer = None

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data)
        if self.serializer.is_valid():
            self.serializer.save()
            if not kwargs.get('heir', False):
                kwargs['status_successfully'] = {"detail": f"Инструкция по восстановлению пароля отправлена на "
                                                           f"{request.data['email']}"}
            return Response(kwargs['status_successfully'], status=status.HTTP_200_OK)
        else:
            return Response(self.serializer.errors, status=status.HTTP_200_OK)


class PasswordResetConfirmView(PasswordResetView):
    """Password confirmation"""
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request, *args, **kwargs):
        status_successfully = {"detail": "Пвроль сброшен, перезайдите с новым паролем"}
        return super().post(request, heir=True, status_successfully=status_successfully)
