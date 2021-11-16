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


class staff(models.Model):
    sname = models.CharField(max_length=50)
    simage = models.CharField(max_length=50)
    splace= models.CharField(max_length=50)
    spin= models.CharField(max_length=50)
    spost = models.CharField(max_length=50)
    yearexperience = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE,default=0)
    DEPID = models.ForeignKey(dept, on_delete=models.CASCADE, default=0)

class schedule(models.Model) :
    day=models.CharField(max_length=50)
    fromtime= models.CharField(max_length=50)
    totime = models.CharField(max_length=50)
    added_date = models.CharField(max_length=50)
    DOCID= models.ForeignKey(doctor, on_delete=models.CASCADE, default=0)

class leavereq(models.Model):
    STAFFID = models.ForeignKey(staff, on_delete=models.CASCADE, default=0)
    leaveneeddate= models.CharField(max_length=50)
    requestdate = models.CharField(max_length=50)
    des = models.CharField(max_length=50)


class attendance(models.Model):
    STAFFID = models.ForeignKey(staff, on_delete=models.CASCADE, default=0)
    checkintime = models.CharField(max_length=50)
    checkouttime = models.CharField(max_length=50)
    date= models.CharField(max_length=50)


class booking(models.Model):
    SCHDID = models.ForeignKey(schedule, on_delete=models.CASCADE, default=0)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    token= models.CharField(max_length=50)
    status= models.CharField(max_length=50)


class user(models.Model):
    userfirstname = models.CharField(max_length=50)
    userlastname = models.CharField(max_length=50)
    uimage = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    uplace= models.CharField(max_length=50)
    upin= models.CharField(max_length=50)
    upost = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE,default=0)
    