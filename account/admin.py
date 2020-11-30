from django.contrib import admin
from .models import Account
# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display=("id","name","email")