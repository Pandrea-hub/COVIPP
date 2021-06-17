from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Person, Rol, Gender
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import datetime
from django.contrib.auth.signals import user_logged_in


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'last_login',
            'username',
            'first_name',
            'last_name',
            'email'
        )


    def create(self, validated_data):
        password = validated_data['password1']
        if validated_data['password1'] == validated_data['password2']:
            del validated_data["password1"]
            del validated_data["password2"]
        user = super(CurrentUserSerializer, self).create(validated_data)
        user.set_password(password)
        user.save()
        return user


class PersonSerializer(serializers.ModelSerializer):
    user = CurrentUserSerializer(many=False, read_only=True)

    class Meta:
        model = Person
        fields = (
            'user',
            'rol',
            'birth_date',
            'gender'
        )

    def create(self, validated_data):  # Crear un registro en la DB
        birth_date = validated_data.pop('birth_date')
        rol = Rol.objects.get(pk=validated_data.pop('rol'))
        gender = Gender.objects.get(pk=validated_data.pop('gender'))
        user_data = validated_data.pop('user')
        user = CurrentUserSerializer.create(CurrentUserSerializer(), validated_data=user_data)
        person, created = Person.objects.update_or_create(user=user, rol=rol, birth_date=birth_date, gender=gender)
        return person


class CustomAuthToken(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            token, created = Token.objects.get_or_create(user=serializer.validated_data['user'])
            user = serializer.validated_data['user']
            user_logged_in.send(sender=user.__class__, request=request, user=user)
            token.delete()
            token = Token.objects.create(user=user)
            token.save()

            person = Person.objects.get(pk=user.pk)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'rol': person.rol_id,
                'gender': person.gender_id,
                'birth_date': person.birth_date
            })
        return Response({
            'Error': 400
        }, status=status.HTTP_400_BAD_REQUEST)


class CustomAuthLogout(ObtainAuthToken):
    def post(self, request):
        return self.logout(request)

    def logout(self, request):
        request.user.auth_token.delete()
        return Response({
            "Success": "Successfully logged out"
        }, status=status.HTTP_200_OK)


obtain_expiring_auth_token = CustomAuthToken.as_view()
