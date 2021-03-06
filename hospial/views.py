from datetime import datetime
import datetime
import random

from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse

from django.shortcuts import render


# Create your views here.

from hospial.models import dept

from hospial.models import login

from hospial.models import staff

from hospial.models import schedule

from hospial.models import *



def login_load(request):

    return render(request,"index.html")


def login_load_post(request):


    user_name = request.POST['username']
    ps_word = request.POST['password']        
    
    if login.objects.filter(username=user_name,password=ps_word).exists():
        login_obj=login.objects.get(username=user_name,password=ps_word)

        request.session["lid"]=str(login_obj.id)


      
        print("true")
        if login_obj.type=="user":
            da=user.objects.get(LOGIN=login_obj.id)
            request.session["id"]=da.id
            return user_home(request)
        elif login_obj.type=="staff":
            da=staff.objects.get(LOGIN=login_obj.id)
            request.session["id"]=da.id
            return staff_home(request)
        elif login_obj.type=="doctor":
            da=doctor.objects.get(LOGIN=login_obj.id)
            request.session["id"]=da.id
            return doctor_home(request)
        elif login_obj.type=="admin":
            return admin_Home(request)
        else:
            return HttpResponse("erro 304")
    else:
        return HttpResponse("no")
        
def admin_temp(request):
    return render(request,"admin/admintemp.html")

def  admin_Home(request):
    
    return render(request,"admin/admin_home.html")

def doctor_home(request):
    b=doctor.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"doctor/doctortemp.html",{'i':b})

def staff_home(request):
    b=staff.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"employes/employtemp.html",{'i':b})

def user_home(request):
    b=user.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"user/usertemp.html",{'i':b})    





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
    fs=FileSystemStorage()
    nam = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    filename=nam+".jpg"
    print(filename)
    fs.save(filename,staff_image)

    url='/media/'+nam+".jpg"

    password=random.randint(1000,9999)


    dept_obj=dept.objects.all()

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

    staff_obj.simage=url

    staff_obj.LOGIN=login_obj

    staff_obj.save()
    

    return render(request, "admin/add_staff.html", {'data':dept_obj})



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

    return admin_add_shedule_load(request)



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

    fs=FileSystemStorage()
    nam = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    filename=nam+".jpg"
    print(filename)
    fs.save(filename,doc_image)

    url='/media/'+nam+".jpg"

    password = random.randint(1000, 9999)


    login_obj = login()

    login_obj.username = doc_email

    login_obj.password = str(password)

    login_obj.type = "doctor"

    login_obj.save()


    doctor_obj=doctor()

    doctor_obj.doctorname=doc_name

    doctor_obj.dimage=url

    doctor_obj.dplace=doc_place

    doctor_obj.dpost=doc_post

    doctor_obj.dpin=doc_pin

    doctor_obj.dgender=doc_gender

    doctor_obj.DEPID_id=doc_department
    doctor_obj.LOGIN_id=login_obj.id

    doctor_obj.licence=doc_lisence

    doctor_obj.experience=doc_experiense

    doctor_obj.phone=doc_number

    doctor_obj.email=doc_email

    doctor_obj.save()
    

    return admin_add_doctor_load(request)




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

    return render(request,"admin/Adminviewdept.html", {'data': res})


def admin_delect_dept(request,deptid):

    dept.objects.filter(id=deptid).delete()

    return HttpResponse("<script>alert('success');window.location='/hospial/admin_adminviewdept_load/'</script>")


def admin_edit_dept(request,depid):

    dep=dept.objects.get(id=depid)

    return render(request,"admin/edit-dept.html",{'data':dep})


def admin_update_dept(request) :

    department = request.POST['username']

    description = request.POST['message'] 

    depid=request.POST['depid']

    dept.objects.filter(id=depid).update(deptname=department,des=description)

    return render(request,"admin/edit-dept.html")     


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


    sid=request.POST['sid']


    if 'image' in request.FILES:

        staff_image = request.FILES['image']

        if staff_image.filename!='':

            staff.objects.filter(id=sid).update(sname=staff_name,simage=staff_image,splace=staff_place,spin=staff_pin,spost=staff_post,phone=staff_number,email=staff_email,sgender=staff_gender)

        else:

            staff.objects.filter(id=sid).update(sname=staff_name,splace=staff_place,spin=staff_pin,spost=staff_post,phone=staff_number,email=staff_email,sgender=staff_gender)

    else:

        staff.objects.filter(id=sid).update(sname=staff_name,splace=staff_place,spin=staff_pin,spost=staff_post,phone=staff_number,email=staff_email,sgender=staff_gender)

    return render(request,"admin/edit-staff.html")


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


def admin_edit_schedule(request,sch):
    shedul=schedule.objects.get(id=sch)
    s1=doctor.objects.all()
    return render(request,"admin/edit-schedule.html",{'data':shedul,'data2':s1})


def admin_update_schedule(request):
    day = request.POST['date']
    f_rom = request.POST['from']
    to = request.POST['to'] 
    shcedu=request.POST['sch']
    schedule.objects.filter(id=sch).update(doctorname=request.POST['select'],day=day,fromtime=f_rom,totime=to)

    return render(request,"admin/edit-schedule.html")  


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

    schedu=schedule.objects.filter()

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
    id=request.session['id']
    book=booking.objects.filter(SCHDID__DOCID__id=id)
    return render(request,"doctor/today_booking.html",{'data':book})



def update_booking(request):

    return render(request,"update_booking.html")


def view_profile(request):

    return render(request,"view_profi(le.html")


def view_schedule(request):

    return render(request,"view_schedule.html")



#employee

def attendance_view(request):

    return render(request,"attendance_view.html")


def leave_status(request):

    return render(request,"leave_status.html")


def view_profile(request):

    return render(request,"view_profile.html")

def adminviewdoctorschedule(request,id):
    sch=schedule.objects.filter(DOCID__id=id)
    return render(request,"admin/bookingSchedule.html",{'data':sch})






#user

def user_registor(request):

    return render(request,"user_registor.html")


def  admin_add_user_load(request):


    return render(request,"user/user-regesister.html")

def admin_user_load_post(request):
    user_name=request.POST['fn']
    user_last=request.POST['f2']
    user_pass=request.POST['pass']
    user_no=request.POST['no']
    user_email=request.POST['mail']
    user_gender=request.POST['g']
    user_dob=request.POST['dob']
    user_profile=request.FILES['dp']

    fs=FileSystemStorage()
    nam = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    filename=nam+".jpg"
    print(filename)
    fs.save(filename,user_profile)

    url='/media/'+nam+".jpg"

    user_place=request.POST['place']
    user_pincode=request.POST['pin']
    user_post=request.POST['post']

    log=login()
    log.username=user_email
    log.password=user_pass
    log.type="user"
    log.save()

    use_r=user()
    use_r.firstname=user_name
    use_r.lastname=user_last
    use_r.email=user_email
    use_r.phone=user_no
    use_r.ugender=user_gender
    use_r.dob=user_dob
    use_r.uimage=url
    use_r.uplace=user_place
    use_r.upin=user_pincode
    use_r.upost=user_post
    use_r.LOGIN=log
    use_r.save()    

    return render(request,"user/user-regesister.html")


def bookingSchedule(request):

     return render(request,"booking/booking.html")

def user_view_doctor(request):

    alldoc=doctor.objects.all()


    dep=dept.objects.all()

    return render(request,"user/view_doctor.html",{'data':alldoc,'dept':dep})



def user_view__doc_serach(request):

    btn=request.POST["btn"]

    dep = dept.objects.all()

    if btn=="search":

        docname=request.POST["n2"]

        res=doctor.objects.filter(doctorname__startswith=docname)

        return render(request, "user/view_doctor.html", {'data': res,'dept':dep})

    elif btn=="go":

        depts=request.POST["select"]

        res = doctor.objects.filter(DEPID_id=depts)

        return render(request, "user/view_doctor.html", {'data': res,'dept':dep})



def user_view_shedule(request,docid):

    schedu=schedule.objects.filter(id=docid)

    return render(request,"user/user_view_sche.html",{'data':schedu})
  


def user_schedule_search(request):

   f_rom= request.POST["d1"]

   to=request.POST["d2"]

   allschedule=schedule.objects.filter(day__range=(f_rom,to))

   return render(request, "user/user_view_sche.html", {'data': allschedule})


def bookings(request,sch):
     shedul=schedule.objects.get(id=sch)
     dat_e=datetime.datetime.now()

     c=booking.objects.filter(SCHDID=shedul)

     if c.exists():
        
        token = c[len(c)-1].token+1
     else:
        token=1 


     booking_obj=booking()
     booking_obj.SCHDID=shedul
     booking_obj.USER_id=request.session['id']
     booking_obj.date=dat_e
     booking_obj.time=dat_e.time()
     booking_obj.token=token
     booking_obj.status="pending"
     booking_obj.save()
     return user_view_doctor((request))

def user_view_booking(request):

    a=booking.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,"user/view_booking.html",{'data':a})

def staff_req(request):
    return render(request,"employes/leave_req.html")

def staff_req_post(request):
    
    req_from = request.POST['from']
    req_to=request.POST['to']
    

    req_msg = request.POST['message']

    req_obj=leavereq()

    req_obj.leave_need_date=req_from
    req_obj.to=req_to
    req_obj.des=req_msg
    req_obj.request_date=datetime.datetime.now().date()
    req_obj.STAFFID=staff.objects.get(LOGIN_id=request.session["lid"])
   
    req_obj.type='staff'
    
    req_obj.save()



    return render(request,"employes/leave_req.html")  

    
def staff_request_view(request):
    b=leavereq.objects.filter(STAFFID__LOGIN_id=request.session['lid'])
    return render(request,"employes/leave_status.html",{'data':b})
  
def staff_view__req_serach(request):

    laave_f=request.POST["n1"]

    res=leavereq.objects.filter(leave_need_date__startswith=laave_f)

    return render(request,"employes/leave_status.html",{'data': res})

def staff_view_profile(request):
    b=staff.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"employes/view_profile.html",{'i':b})

def staff_cancel_bk(request,leaveid):
     leavereq.objects.filter(id=leaveid).delete()

     return HttpResponse("<script>alert('success');window.location='/hospial/staff_request_view/'</script>")
 
def user_view_profile(request):
    b=user.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"user/user_view_profile.html",{'i':b})

def doctor_view_profile(request):
     b=doctor.objects.get(LOGIN_id=request.session['lid'])
     return render(request,"doctor/view_profile.html",{'i':b})


def doc_req(request):
    return render(request,"doctor/doc_leavereq.html")



def doc_req_post(request):
    
    req_from = request.POST['from']

    req_to = request.POST['to']

    req_msg = request.POST['message']
    import datetime
    req_obj=doctorleav()
    req_obj.fro_m=req_from
    req_obj.to=req_to
    req_obj.des=req_msg
    req_obj.reqdate=datetime.datetime.now().date()
    req_obj.DOCID=doctor.objects.get(LOGIN_id=request.session["lid"])    
    req_obj.save()



    return render(request,"doctor/doc_leavereq.html")  



def doc_request_view(request):
    b=doctorleav.objects.filter(DOCID__LOGIN_id=request.session['lid'])
    return render(request,"doctor/doc_leav_status.html",{'data':b})
    

def doc_view__req_serach(request):

    laave_f=request.POST["n1"]

    res=doctorleav.objects.filter(fro_m__startswith=laave_f)

    return render(request,"doctor/doc_leav_status.html",{'data': res})

def doc_cancel_bk(request,leaveid):
     doctorleav.objects.filter(id=leaveid).delete()

     return HttpResponse("<script>alert('success');window.location='/hospial/doc_request_view/'</script>")



def admin_lev_view_doc(request):
     levdoc=doctorleav.objects.all()

     return render(request,"admin/admin_view_lv.html",{'data':levdoc})

def admin_stafflv_view(request):
    leavstaff=leavereq.objects.all()
    return render(request,"admin/staff_lvreq_view.html",{'data':leavstaff})