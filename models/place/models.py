from django.db import models
from models.type_place.models import TypePlace


class Place(models.Model):
    title = models.CharField(max_length=60, default=None)
    #icon = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    draggable = models.BooleanField(default=False)
    fragment = models.CharField(max_length=60, default=None)
    longitude = models.CharField(max_length=60, default=None)
    latitude = models.CharField(max_length=60, default=None)
    type_place = models.ForeignKey(TypePlace, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
