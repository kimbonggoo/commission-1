from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('first_name', 'uid', 'exchange', 'amount', 'phone', 'email')
    
    fieldsets = (
        (
        '회원정보', 
            {'fields': 
                (
                    'username',
                    'first_name',
                    'phone',
                    'email',
                    'exchange',
                    'uid',
                    'amount',
                    'use_check',
                    'pi_check',
                    'upper_uid1',
                    'upper_uid2',
                    'lower_uids',
                    'use_rebate',
                )
            }
        ),
    )
