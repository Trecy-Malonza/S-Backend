from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    tsc_number = models.CharField(max_length=100, default="DEFAULT_TSC_NUMBER")
    email = models.EmailField(unique=True)
    region = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    teachers_id = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
