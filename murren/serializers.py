from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode as uid_decode

# drf
from rest_framework import serializers

# local
from murren.models import Murren


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reset_form_send = None

    @staticmethod
    def get_email_options():
        return {'domain_override': ''}

    def validate_email(self, value):
        murren = Murren.objects.filter(email=value)

        if not murren:
            detail = F'email: {value} - не зарегистрирован'
            raise serializers.ValidationError(detail=detail)
        elif not murren[0].is_active:
            detail = 'Активируйте пожалуйста свой аккаунт'
            raise serializers.ValidationError(detail=detail)

        self.reset_form_send = PasswordResetForm(data=self.initial_data)
        if not self.reset_form_send.is_valid():
            raise serializers.ValidationError(self.reset_form_send.errors)
        return value

    def save(self):
        request = self.context.get('request')
        context = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL', 'admin@gmail.com'),
            'request': request,
            'email_template_name': 'murren/password_reset_email.txt',
        }
        context.update(self.get_email_options())
        self.reset_form_send.save(**context)


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password1 = serializers.CharField(label='Новый пароль', max_length=128, write_only=True,
                                          style={'input_type': 'password'})
    new_password2 = serializers.CharField(label='Подтвердите пароль', max_length=128, write_only=True,
                                          style={'input_type': 'password'})

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_password_form = None

    def validate(self, data):
        request_kwargs = self.context['request'].resolver_match.kwargs

        try:
            uid = force_text(uid_decode(request_kwargs['uidb64']))
            user = get_object_or_404(Murren, pk=uid)
        except ():
            detail = {'uid': 'Не верный uid'}
            raise serializers.ValidationError(detail=detail)

        self.set_password_form = SetPasswordForm(user=user, data=data)

        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        if not default_token_generator.check_token(user, request_kwargs['token']):
            detail = {'token': 'Не верный token или истек срок сброса пароля'}
            raise serializers.ValidationError(detail=detail)

        return data

    def save(self):
        self.set_password_form.save()
