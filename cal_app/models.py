from django.db import models

# Create your models here.
class rem_result(models.Model):
    first_num = models.CharField(max_length=20)
    sec_num = models.CharField(max_length=20)
    cal_type = models.CharField(max_length=4)
    cal_result = models.CharField(max_length=20)
    col1 = models.CharField(blank=True,max_length=2)
    col2 = models.CharField(blank=True,max_length=2)
    col3 = models.CharField(blank=True,max_length=2)
    col4 = models.CharField(blank=True,max_length=2)
    col5 = models.CharField(blank=True,max_length=2)
