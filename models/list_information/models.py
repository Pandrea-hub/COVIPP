from django.db import models
from models.person.models import Person
from models.place.models import Place
from models.vaccine.models import Vaccine


class ListInformation(models.Model):
    date = models.DateField(default=None)
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, null=True, blank=True, on_delete=models.CASCADE)
    applied_doses = models.IntegerField(default=0)
    place = models.ForeignKey(Place, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.person

    class Meta:
        ordering = ('person',)


class CompleteInformationView(models.Model):
    days = models.IntegerField()
    first_dose_date = models.CharField(max_length=100, default=None)
    second_dose_date = models.CharField(max_length=100, default=None)
    first_name = models.CharField(max_length=100, default=None)
    last_name = models.CharField(max_length=100, default=None)
    age = models.IntegerField()
    vaccine_name = models.CharField(max_length=100, default=None)
    number_doses =models.IntegerField()
    applied_doses = models.IntegerField()
    name_place = models.CharField(max_length=100, default=None)


    def __str__(self):
        return '%s: %s' % (self.first_name, self.applied_doses)

    class Meta:
        managed = False
        db_table = 'vw_list_information'
        ordering = ('id',)
