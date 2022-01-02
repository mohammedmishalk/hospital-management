import datetime
import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from hospial.models import dept
from hospial.models import login
from hospial.models import staff
from hospial.models import schedule
from hospial.models import *


def login_load(request):
    return render(request,"login.html")

def login_load_post(request):
    user_name = request.POST['username']
    ps_word = request.POST['password']
    login_obj=login()
    login_obj.username=user_name
    login_obj.password=ps_word
    login_obj.save()
    return render(request, 'login.html')

def  admin_Home(request):
    return render(request,"admin/admin_home.html")


def  admin_add_staff_load(request):
    dept_obj=dept.objects.all()
    return render(request,"admin/add_staff.html", {'data':dept_obj})

def admin_add_staff_load_post(request):
    staff_name=request.POST['staffname']
    staff_place = request.POST['place']
    staff_pin = request.POST['pin']
    staff_post = request.POST['post']
    staff_department = request.POST['select']
    staff_gender = request.POST['fav_language']
    staff_experiense = request.POST['exp']
    staff_email = request.POST['email']
    staff_number = request.POST['no']
    staff_image = request.FILES['image']
    password=random.randint(1000,9999)



    login_obj=login()
    login_obj.username=staff_email
    login_obj.password=str(password)
    login_obj.type="staff"
    login_obj.save()


    staff_obj=staff()
    staff_obj.sname=staff_name
    staff_obj.simage=""
    staff_obj.splace=staff_place
    staff_obj.spost=staff_post
    staff_obj.spin=staff_pin
    staff_obj.DEPID_id=staff_department
    staff_obj.sgender=staff_gender
    staff_obj.xperience=staff_experiense
    staff_obj.phone=staff_number
    staff_obj.email=staff_email
    staff_obj.simage=staff_image
    staff_obj.LOGIN=login_obj
    staff_obj.save()
    
    return render(request, "admin/add_staff.html")


def admin_add_shedule_load(request):
    doc_obj = doctor.objects.all()

    return render(request,"admin/add-shedule.html",{'data':doc_obj})

def admin_add_shedule_load_post(request):
    docid= request.POST['select']
    day = request.POST['date']
    f_rom = request.POST['from']
    to = request.POST['to']
    shedule_obj=schedule()

    shedule_obj.day=day
    shedule_obj.fromtime=f_rom
    shedule_obj.totime=to
    shedule_obj.DOCID_id=docid
    shedule_obj.added_date=datetime.datetime.now()
    shedule_obj.save()
    return render(request, "admin/add-shedule.html")


def admin_add_doctor_load(request):
    dept_obj = dept.objects.all()
    return render(request,"admin/adddoctor.html", {'data':dept_obj})

def admin_add_doctor_load_post(request):
    doc_name=request.POST['name']
    doc_place = request.POST['place']
    doc_pin = request.POST['pin']
    doc_post = request.POST['post']
    doc_department = request.POST['select']
    doc_gender = request.POST['fav_language']
    doc_experiense = request.POST['exp']
    doc_email = request.POST['email']
    doc_lisence = request.FILES['file']
    doc_number = request.POST['no']
    doc_image = request.FILES['image']
    password = random.randint(1000, 9999)

    login_obj = login()
    login_obj.username = doc_email
    login_obj.password = str(password)
    login_obj.type = "doctor"
    login_obj.save()

    doctor_obj=doctor()
    doctor_obj.doctorname=doc_name
    doctor_obj.dimage=doc_image
    doctor_obj.dplace=doc_place
    doctor_obj.dpost=doc_post
    doctor_obj.dpin=doc_pin
    doctor_obj.dgender=doc_gender
    doctor_obj.DEPID_id=doc_department
    doctor_obj.licence=doc_lisence
    doctor_obj.experience=doc_experiense
    doctor_obj.phone=doc_number
    doctor_obj.email=doc_email
    doctor_obj.save()
    
    return render(request, "admin/adddoctor.html")



def admin_add_dept_load(request):
    return render(request,"admin/amindadd-det.html")

def admin_add_dept_post(request):
    department = request.POST['username']
    description = request.POST['message']
    dept_obj=dept()
    dept_obj.deptname=department
    dept_obj.des=description

    dept_obj.save()
    return render(request,"admin/amindadd-det.html")


def admin_adminviewdept_load(request):
    alldept=dept.objects.all()
    return render(request,"admin/Adminviewdept.html",{'data':alldept})
def admin_view_serach(request):
    depname=request.POST["n1"]
    res=dept.objects.filter(deptname__startswith=depname)
    return render(request, "admin/Adminviewdept.html", {'data': res})

def admin_delect_dept(request,deptid):
    dept.objects.filter(id=deptid).delete()
    return HttpResponse("<script>alert('success');window.location='/hospial/admin_adminviewdept_load/'</script>")

def admin_edit_dept(request,depid):
    dep=dept.objects.get(id=depid)
    return render(request,"admin/edit-dept.html",{'data':dep})

def admin_edit_staff(request,sid):
    staf=staff.objects.get(id=sid)
    dept_obj=dept.objects.all()
    return render(request,"admin/edit-staff.html",{'data':staf,'dept':dept_obj})

def admin_update_staff(request) :   
    staff_name=request.POST['staffname']
    staff_place = request.POST['place']
    staff_pin = request.POST['pin']
    staff_post = request.POST['post']
    staff_department = request.POST['select']
    staff_gender = request.POST['fav_language']
    staff_experiense = request.POST['exp']
    staff_email = request.POST['email']
    staff_number = request.POST['no']
    staff_image = request.FILES['image']
    

def admin_edit_doctor(request,did):
    doc=doctor.objects.get(id=did)
    dept_obj=dept.objects.all()
    return render(request,"admin/editdoctor.html",{'data':doc,'dept':dept_obj})

def admin_update_doctor(request):
    doc_name=request.POST['name']
    doc_place = request.POST['place']
    doc_pin = request.POST['pin']
    doc_post = request.POST['post']
    doc_department = request.POST['select']
    doc_gender = request.POST['fav_language']
    doc_experiense = request.POST['exp']
    doc_email = request.POST['email']
    doc_number = request.POST['no']
    did=request.POST['did']
    print(did)
    # if 'file' in request.FILES:
    #      doc_lisence = request.FILES['file']
    if 'image' in request.FILES:
          doc_image = request.FILES['image']
          if doc_image.filename!='':
              doctor.objects.filter(id=did).update(doctorname=doc_name,dplace=doc_place,dpin=doc_pin,dpost=doc_post,experience=doc_experiense,phone=doc_number,email=doc_email,dgender=doc_gender,dimage=doc_image)
          else:
               doctor.objects.filter(id=did).update(doctorname=doc_name,dplace=doc_place,dpin=doc_pin,dpost=doc_post,experience=doc_experiense,phone=doc_number,email=doc_email,dgender=doc_gender)
    else :
          doctor.objects.filter(id=did).update(doctorname=doc_name,dplace=doc_place,dpin=doc_pin,dpost=doc_post,experience=doc_experiense,phone=doc_number,email=doc_email,dgender=doc_gender)
    return render(request,"admin/editdoctor.html")

def admin_edit_schedule(request,shid):
    shedul=schedule.objects.get(id=shid)
    return render(request,"admin/edit-schedule.html",{'data':shedul})

def admin_leave_req(request):
    return render(request,"admin/leave-request.html")

def admin_view_attends(request):

    return render(request,"admin/view-attends.html")


def admin_view_doctor(request):
    alldoc=doctor.objects.all()

    dep=dept.objects.all()
    return render(request,"admin/view-doctor.html",{'data':alldoc,'dept':dep})

def admin_view__doc_serach(request):
    btn=request.POST["btn"]
    dep = dept.objects.all()
    if btn=="search":
        docname=request.POST["n2"]
        res=doctor.objects.filter(doctorname__startswith=docname)
        return render(request, "admin/view-doctor.html", {'data': res,'dept':dep})
    elif btn=="go":
        depts=request.POST["select"]
        res = doctor.objects.filter(DEPID_id=depts)
        return render(request, "admin/view-doctor.html", {'data': res,'dept':dep})



def admin_delect_doctor(request,docid):
    doctor.objects.filter(id=docid).delete()
    return HttpResponse("<script>alert('success');window.location='/hospial/admin_view_doctor/'</script>")


def admin_view_shedule(request):
    schedu=schedule.objects.all()
    return render(request,"admin/view-schedule.html",{'data':schedu})

def admin_schedule_search(request):
   f_rom= request.POST["d1"]
   to=request.POST["d2"]
   allschedule=schedule.objects.filter(day__range=(f_rom,to))
   return render(request, "admin/view-schedule.html", {'data': allschedule})

def admin_delect_schedule(request,scheduleid):
    schedule.objects.filter(id=scheduleid).delete()
    return HttpResponse("<script>alert('success');window.location='/hospial/admin_view_shedule/'</script>")


def admin_view_staff(request):
    alstaff=staff.objects.all()
    dep = dept.objects.all()
    return render(request,"admin/viewstaff.html",{'data':alstaff,'dept':dep})


def admin_view__staff_serach(request):
    btn=request.POST["btn"]
    dep = dept.objects.all()
    if btn=="search":
        staffname=request.POST["n2"]
        res=staff.objects.filter(sname__startswith=staffname)
        return render(request, "admin/viewstaff.html", {'data': res,'dept':dep})
    elif btn=="go":
        depts=request.POST["select"]
        res = staff.objects.filter(DEPID_id=depts)
        return render(request, "admin/viewstaff.html", {'data': res,'dept':dep})

def admin_delect_staff(request,staffid ):
        staff.objects.filter(id=staffid).delete()
        return HttpResponse("<script>alert('success');window.location='/hospial/admin_view_staff/'</script>")

#doctor

def today_booking(request):
    return render(request,"today_booking.html")


def update_booking(request):
    return render(request,"update_booking.html")

def view_profile(request):
    return render(request,"view_profile.html")

def view_schedule(request):
    return render(request,"view_schedule.html")


#employee
def attendance_view(request):
    return render(request,"attendance_view.html")

def leave_status(request):
    return render(request,"leave_status.html")

def view_profile(request):
    return render(request,"view_profile.html")

#user
def user_registor(request):
    return render(request,"user_registor.html")














