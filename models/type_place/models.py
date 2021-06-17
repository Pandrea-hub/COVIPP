from django.db import models


class TypePlace(models.Model):
    name = models.CharField(max_length=60, default=None)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
