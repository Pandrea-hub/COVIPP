from django.db import models


class Gender(models.Model):
    name = models.CharField(max_length=10, default=None)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
