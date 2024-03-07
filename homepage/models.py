from django.db import models

# Create your models here.

class Student(models.Model):

    id=models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    Total_mark = models.IntegerField()
    register_number = models.IntegerField(null=True)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=25,null=True)


    def __str__(self):
        return self.first_name