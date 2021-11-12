from django.db import models

# Create your models here.
class DataModel(models.Model):
    name = models.CharField(max_length = 200)
    department = models.CharField(max_length=300)
    age = models.IntegerField()


    def __str__(self):
        return self.name