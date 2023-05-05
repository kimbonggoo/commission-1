from django.db import models


class TapbitData(models.Model):
    uid = models.CharField(max_length=8)
    rebate = models.CharField(max_length=200)
    upper_rebate = models.CharField(max_length=200)
    total_rebate = models.CharField(max_length=200)
