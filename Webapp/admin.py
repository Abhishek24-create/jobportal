from django.contrib import admin
from Webapp.models import adminlogin
class Admin(admin.ModelAdmin):
    list_display = ['username','password']
admin.site.register(adminlogin,Admin)

