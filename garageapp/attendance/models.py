from django.db import models

# Create your models here.


class Address(models.Model):
    address_street = models.CharField(max_length=200)
    address_number = models.IntegerField()
    localidad = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    provincia = models.CharField(max_length=200)


class Location(models.Model):
    name = models.CharField(max_length=200, blank=False)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)


class RehearsalType(models.Model):
    name = models.CharField(max_length=50, blank=False)


class Rehearsal(models.Model):
    rehearsal_date = models.DateTimeField(name='fecha')
    location = models.ForeignKey(Location, on_delete=models.RESTRICT)
    rehearsal_type = models.ForeignKey(
        RehearsalType, on_delete=models.RESTRICT)


class ChoirSinger(models.Model):
    id_number = models.IntegerField(primary_key=True, blank=False, unique=True)
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    date_of_birth = models.DateTimeField()
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)


class Attendance(models.Model):
    singer = models.ForeignKey(ChoirSinger, on_delete=models.RESTRICT)
    rehearsal = models.ForeignKey(Rehearsal, on_delete=models.RESTRICT)
