from django.contrib import admin
from . import models

@admin.register(models.TapbitData)
class DataAdmin(admin.ModelAdmin):
    
    list_display = (
        'uid',
        'rebate',
        'upper_rebate',
        'total_rebate',
    )
