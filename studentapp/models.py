from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length = 10)
    last_name = models.CharField(max_length = 15)
    middle_name = models.CharField(max_length = 15)
    date = models.DateField()
    foto = models.FileField(upload_to = None)
    stud_bilet = models.CharField(max_length = 100)
    stud_group = models.CharField(max_length = 20)

class Stud_group(models.Model):
    name_group = models.CharField(max_length = 50)
    king_group = models.CharField(max_length = 50)