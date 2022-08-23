from django.contrib import admin
from .models import Device,Clinic
# Register your models here.
@admin.register(Device)
class AdminDevice(admin.ModelAdmin):
    list_display=['device_id','is_login','is_active','reg_user','update_user','cdate','udate']
@admin.register(Clinic)
class AdminClinic(admin.ModelAdmin):
    list_display=['device','name','city','cdate','udate']