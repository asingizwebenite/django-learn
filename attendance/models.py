from django.db import models
from django.utils import timezone

# Create your models here.
class Farmer(models.Model):
    name=models.CharField()
    farm=models.CharField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='M')
    YES_NO_CHOICES = [
        (True, 'Yes'),
        (False, 'No'),
    ]
    is_contracted = models.BooleanField(choices=YES_NO_CHOICES, default=False)


    class Meta:
        db_table="farmer"
    
    def __str__(self):
       return self.name




   
class Attendance(models.Model):
    date=models.DateField(default=timezone.now)
    is_present=models.BooleanField()
    farmer= models.ForeignKey(Farmer, on_delete=models.CASCADE)


    class Meta:
        db_table="attendance"


