from django.db import models
from django.contrib.auth.models import User
from models.rol.models import Rol
from models.gender.models import Gender



class Person(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, null=True, blank=True, on_delete=models.CASCADE)
    birth_date = models.DateField(default=None)
    gender = models.ForeignKey(Gender, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return 'User {}'.format(self.user)

    class Meta:
        ordering = ('rol',)




