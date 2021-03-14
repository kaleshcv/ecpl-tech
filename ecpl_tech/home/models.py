from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Profile(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    emp_name = models.CharField(max_length=30)
    emp_id=models.IntegerField()
    email=models.EmailField(default='emp@ecpl.com',null=True)
    phone=models.IntegerField(default=999999999)

    def __str__(self):
        return self.emp_name

class Cpu(models.Model):
    item_name=models.CharField(default='CPU',max_length=10)
    item_id=models.IntegerField(default=1)
    in_date=models.DateField()
    serial_no=models.CharField(max_length=50,unique=True)
    ecpl_tag_name=models.CharField(max_length=30,unique=True)
    processor=models.CharField(max_length=20)
    ram=models.CharField(max_length=20)
    hd_type=models.CharField(max_length=30)
    hd_size=models.CharField(max_length=30)
    hd_serial_no=models.CharField(max_length=100)
    make=models.CharField(max_length=30)
    model=models.CharField(max_length=100)
    vendor=models.CharField(max_length=50)
    system_name=models.CharField(max_length=50)

    in_stock = models.BooleanField(default=False)
    out = models.BooleanField(default=False)
    assigned = models.BooleanField(default=False)
    service = models.BooleanField(default=False)

    def __str__(self):
        return self.serial_no


class Desktop(models.Model):
    item_name = models.CharField(default='DESKTOP', max_length=20)
    item_id = models.IntegerField(default=2)
    in_date = models.DateField(default=datetime.date.today)
    serial_no = models.CharField(max_length=50, unique=True)
    ecpl_tag_name = models.CharField(max_length=30, unique=True)
    processor = models.CharField(max_length=20)
    ram = models.CharField(max_length=20)
    hd_type = models.CharField(max_length=30)
    hd_size = models.CharField(max_length=30)
    hd_serial_no = models.CharField(max_length=100)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=100)
    vendor = models.CharField(max_length=50)
    system_name = models.CharField(max_length=50)

    in_stock=models.BooleanField(default=True)
    out=models.BooleanField(default=False)
    assigned=models.BooleanField(default=False)
    service=models.BooleanField(default=False)

    def __str__(self):
        return self.serial_no






class Assigned(models.Model):
    date=models.DateField()
    item=models.CharField(max_length=50)
    item_serial=models.CharField(max_length=100)
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=50)
    assigned_by=models.CharField(max_length=50)
    campaign=models.CharField(max_length=100)
    return_status=models.BooleanField(default=False)


class ServiceCpu(models.Model):
    date = models.DateField()
    it_name=models.CharField(max_length=50)
    vendor=models.CharField(max_length=50)
    desc=models.TextField()
    item_serial=models.CharField(max_length=50)
    service_status=models.BooleanField(default=True)

class ReturnCpu(models.Model):
    date = models.DateField()
    it_name=models.CharField(max_length=50)
    vendor=models.CharField(max_length=50)
    desc=models.TextField()
    item_serial=models.CharField(max_length=50)