# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import generics
from .models import Person, Rol, User
from .serializers import PersonSerializer
from django.shortcuts import get_object_or_404
from validate_email import validate_email
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
import django.contrib.auth.password_validation as validators
from django.contrib.auth import password_validation
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

from rest_framework.permissions import IsAuthenticated, AllowAny
import re


def home(request):
    template = "home.html"
    context = {}
    return render(request, template, context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        return HttpResponse(
            '<b>COVIPP</b> Gracias por tu confirmación de correo electrónico. Una vez confirmados tus datos se te activará la cuenta y se te enviará un correo notificándolo para que puedas iniciar con COVIPP!.')
    else:
        return HttpResponse('Link de activación inválido!')

@permission_classes([AllowAny])
class PersonView(APIView):
    def get(self, format=None):  # se crea el GET
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)

    def clean_email(self, data):
        email = data['email']
        try:
            match = User.objects.get(email=email)
            print(match)
        except User.DoesNotExist:
            return True
        raise serializers.ValidationError({"Error el email no existe": 102})
        return False

    def clean_username(self, data):
        username = data["username"]
        try:
            match = User.objects.get(username=username)
            print(match)
        except User.DoesNotExist:
            return True
        raise serializers.ValidationError({"Error el usuario no existe": 103})
        return False

    def auth_password_strength(self, value):
        try:
            password_validation.validate_password(value, self)
        except:
            raise serializers.ValidationError({"Error no se pudo validar la contraseña": 108})
            return False
        return True

    def validate_password_strength(self, value):
        min_length = 8
        if len(value) < min_length:
            raise serializers.ValidationError({" Error la contraseña debe tener 8 caracteres como minimo": 104})

        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError({"Error la contraseña debe tener un digito": 105})

        if not any(char.isalpha() for char in value):
            raise serializers.ValidationError({"Error la contraseña debe tener una letra del alfabeto": 106})

    def post(self, request):
        data = request.data.get('user')
        serializer = PersonSerializer(data=request.data)
        min_length = 6
        if not data['username']:
            raise serializers.ValidationError({"Error no hay usuario": 108})

        if not re.search(r'^\w+$', data['username']):
            raise serializers.ValidationError({"Error el nombre de usuario debe ser alfanumerico": 109})

        if len(data['username']) < min_length:
            raise serializers.ValidationError({"Error el usuario debe tener minimo 6 caracteres": 110})

        if not request.data.get('rol'):
            raise serializers.ValidationError({"Error no hay rol": 111})

        if not request.data.get('gender'):
            raise serializers.ValidationError({"Error no hay un genero": 114})

        if not request.data.get('birth_date'):
            raise serializers.ValidationError({"Error no hay una fecha de nacimiento": 115})

        if data['password1'] != data['password2']:
            raise serializers.ValidationError({"Error la contraseña no coincide": 112})
        else:
            self.validate_password_strength(data['password1'])

        if not validate_email(data['email']):
            raise serializers.ValidationError({'Error el email no es valido': 113})

        if not self.clean_email(data):
            raise serializers.ValidationError(self.clean_email(data))

        if not self.clean_username(data):
            raise serializers.ValidationError(self.clean_email(data))

        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            user = User.objects.get(username=data['username'])
            current_site = get_current_site(request)
            message = render_to_string('active_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Welcome to COVIPP'
            to_email = data['email']
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny])
class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

