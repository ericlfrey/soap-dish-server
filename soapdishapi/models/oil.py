from django.db import models


class Oil(models.Model):

    name = models.CharField(max_length=50)
    sap = models.DecimalField(max_digits=5, decimal_places=3)
