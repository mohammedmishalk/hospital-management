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
    dgender = models.CharField(max_length=50, default="")
    experience = models.CharField(max_length=50)
    licence= models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE,default=1)
    DEPID = models.ForeignKey(dept, on_delete=models.CASCADE, default=1)


class staff(models.Model):
    sname = models.CharField(max_length=50)
    simage = models.CharField(max_length=50)
    splace= models.CharField(max_length=50)
    spin= models.CharField(max_length=50)
    spost = models.CharField(max_length=50)
    sgender = models.CharField(max_length=50,default="")
    xperience = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE,default=1)
    DEPID = models.ForeignKey(dept, on_delete=models.CASCADE, default=1)

class schedule(models.Model) :
    day=models.CharField(max_length=50)
    fromtime= models.CharField(max_length=50)
    totime = models.CharField(max_length=50)
    added_date = models.CharField(max_length=50)
    DOCID= models.ForeignKey(doctor, on_delete=models.CASCADE, default=1)

class  leavereq(models.Model):
    STAFFID = models.ForeignKey(staff, on_delete=models.CASCADE, default=1)
    leave_need_date= models.CharField(max_length=50,default='1')
    to=models.CharField(max_length=50 ,default='1')
    request_date = models.CharField(max_length=50 ,default='1')
    des = models.CharField(max_length=50 ,default='1')

class doctorleav(models.Model):
    fro_m=models.CharField(max_length=50,default='1')
    to=models.CharField(max_length=50,default='1')
    des=models.CharField(max_length=50,default='1')
    DOCID= models.ForeignKey(doctor, on_delete=models.CASCADE, default=1)
    reqdate=models.CharField(max_length=50 ,default='1')

class attendance(models.Model):
    STAFFID = models.ForeignKey(staff, on_delete=models.CASCADE, default=1)
    checkin_time = models.CharField(max_length=50)
    checkout_time = models.CharField(max_length=50)
    date= models.CharField(max_length=50)


class user(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    uimage = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    ugender = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    uplace= models.CharField(max_length=50)
    upost = models.CharField(max_length=50)
    upin= models.CharField(max_length=50)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE,default=1)


class booking(models.Model):
    USER=models.ForeignKey(user, on_delete=models.CASCADE, default=1) 
    SCHDID = models.ForeignKey(schedule, on_delete=models.CASCADE, default=1)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    token= models.IntegerField(default=1)
    status= models.CharField(max_length=50)


  