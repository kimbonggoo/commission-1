from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from parsed_data.models import TapbitData

class User(AbstractUser):
    # username
    # first_name
    # last_name
    # email 
    # is_staff
    # is_active
    # date_joined
    
    phone_num_regex = RegexValidator(regex = r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone = models.CharField(max_length=11, validators= [phone_num_regex])
    exchange = models.CharField(max_length=20)
    uid = models.CharField(max_length=8)
    amount = models.CharField(max_length=15, blank=True)
    use_check = models.BooleanField(default=True)
    pi_check = models.BooleanField(default=True)
    upper_uid1 = models.CharField(max_length=8, blank=True)
    upper_uid2 = models.CharField(max_length=8, blank=True)
    lower_uids = models.CharField(max_length=500, blank=True)
    use_rebate = models.CharField(max_length=100, blank=True, default='0')
    data = models.ForeignKey(TapbitData, on_delete=models.CASCADE, related_name='users', blank=True, null=True)
