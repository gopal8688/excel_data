from django.db import models


class File_input(models.Model):
    file = models.FileField(upload_to='media/')

class Save_data(models.Model):
    no = models.BigIntegerField()
    product = models.CharField(max_length=200)
    proposal_no = models.BigIntegerField()
    inwardnumber = models.CharField(max_length=250)
    currentworkstep = models.CharField(max_length=200)
    names = models.CharField(max_length=100)
    customer_names = models.CharField(max_length=200)

