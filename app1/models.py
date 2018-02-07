from django.db import models

# Create your models here.
class User(models.Model):
    firstName   = models.CharField(max_length=20)
    lastName    = models.CharField(max_length=20)
    emailId     = models.EmailField(unique=True)
    number      = models.CharField(max_length=10)
    age         = models.IntegerField()

    def __str__(self):
        x = self.firstName + " " + self.lastName
        return x

    def __repr__(self):
        x = self.firstName + " " + self.lastName
        return x
