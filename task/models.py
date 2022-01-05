from django.db import models

# Create your models here.
class Vehicle(models.Model):
    plate = models.CharField(max_length=10)


class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, blank=True, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Operation(models.Model):
    name = models.CharField(max_length=128)


class Bin(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    operation = models.ManyToManyField(Operation, related_name='bin', through='BinOperation')


class BinOperation(models.Model):
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    collection_frequency = models.IntegerField()
    last_collection = models.DateTimeField(auto_now_add=True)