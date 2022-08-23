from turtle import update
from django.db import models

# Create your models here.
class Device(models.Model):
    device_id=models.CharField(max_length=100,verbose_name='Device ID')
    is_login=models.BooleanField(default=False,verbose_name='Is In Use Now?')
    is_active=models.BooleanField(default=True,verbose_name='Is Active?')
    reg_user=models.CharField(max_length=100,verbose_name='Register By Username')
    update_user=models.CharField(max_length=100,verbose_name='Update By Username')
    cdate=models.DateTimeField(auto_created=True,auto_now_add=True,verbose_name='Created Date')
    udate=models.DateTimeField(auto_created=True,auto_now_add=True,verbose_name='Update Date')
    
    class Meta:
        ordering=['-udate']
    
    def __str__(self):
        return f'Device Id ; {self.device_id} | Active : {self.is_active} | In Use : {self.is_login}'

class Clinic(models.Model):
    device=models.ForeignKey(Device,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Device')
    name=models.CharField(max_length=100,default='',verbose_name='Clinic Name')
    city=models.CharField(max_length=100,default='',verbose_name='Clinic City')
    cdate = models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='Created Date')
    udate = models.DateTimeField(auto_created=True, auto_now=True, verbose_name='Updated Date')

    class Meta:
        ordering = ["-udate"]

    def __str__(self):
        return "Clinic Name : " + str(self.name)
