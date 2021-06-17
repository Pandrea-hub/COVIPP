from django.db import models


class Rol(models.Model):
    name = models.CharField(max_length=60, default=None)
    editList = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)



