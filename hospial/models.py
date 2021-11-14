from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=50)




class dept(models.Model):
    deptname = models.CharField(max_length=50)
    des = models.CharField(max_length=200)



class doctor(models.Model):
    doctorname = models.CharField(max_length=50)
    dimage = models.CharField(max_length=50)
    dplace= models.CharField(max_length=50)
    dpin= models.CharField(max_length=50)
    dpost = models.CharField(max_length=50)
    yearexperience = models.CharField(max_length=50)
    licence= models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE,default=0)
    DEPID = models.ForeignKey(dept, on_delete=models.CASCADE, default=0)



