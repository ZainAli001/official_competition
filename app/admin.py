from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(User)
admin.site.register(CommissionPayout)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email','referred_by','subscription_amount','commission_earned')
admin.site.register(User,UserAdmin)