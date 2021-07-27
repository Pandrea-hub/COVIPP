from django.db import models
from models.contagion_type.models import ContagionType
from models.person.models import Person


class Cases(models.Model):
    date = models.DateField(default=None)
    contagion_type = models.ForeignKey(ContagionType, null=True, blank=True, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.date

    class Meta:
        ordering = ('date',)


class CasesSymptomView(models.Model):
    cases_id = models.IntegerField()
    symptom_day = models.CharField(max_length=60, default=None)
    contagion_day = models.CharField(max_length=60, default=None)
    infectious_day = models.CharField(max_length=50, default=None)
    not_contagion_day = models.CharField(max_length=60, default=None)
    not_covid = models.CharField(max_length=60, default=None)
    first_name = models.CharField(max_length=50, default=None)
    last_name = models.CharField(max_length=50, default=None)



    def __str__(self):
        return '%s: %s' % (self.first_name, self.symptom_day)


    class Meta:
        managed = False
        db_table = 'vw_symptom_cases'
        ordering = ('id',)


class CasesContagionView(models.Model):
    cases_id = models.IntegerField()
    contagion_day = models.CharField(max_length=50, default=None)
    infectious_day = models.CharField(max_length=50, default=None)
    symptom_day = models.CharField(max_length=50, default=None)
    not_infectious_day = models.CharField(max_length=50, default=None)
    free_covid = models.CharField(max_length=50, default=None)
    first_name = models.CharField(max_length=50, default=None)
    last_name = models.CharField(max_length=50, default=None)

    def __str__(self):
        return '%s: %s' % (self.first_name, self.contagion_day)

    class Meta:
        managed = False
        db_table = 'vw_contagion_cases'
        ordering = ('id',)