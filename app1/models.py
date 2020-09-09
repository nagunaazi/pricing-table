from django.db import models

# Create your models here.



class Pricing_table(models.Model):
    ID = models.IntegerField(primary_key=True)
    Plan_Name = models.CharField(max_length=60)
    Plan_Formula = models.CharField(max_length=60)
    Location = models.CharField(max_length=30)
    Plan_Status = models.CharField(max_length=30)
    Created_Date = models.DateField(blank=True,null=True)
    Updated_Date = models.DateField(blank=True,null=True)

