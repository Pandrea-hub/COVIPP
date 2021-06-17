from django.db import models


class Vaccine(models.Model):
    name = models.CharField(max_length=50, default=None)
    days = models.IntegerField(default=None)
    number_doses = models.IntegerField(default=None)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
