from django.db import models


class Deposits(models.Model):
    deposit = models.CharField(max_length=30)
    term = models.CharField(max_length=30)
    rate = models.CharField(max_length=30)
    interest = models.CharField(max_length=30)

