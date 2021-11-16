from django.shortcuts import render

# Create your views here.

def login_load(request):
    return render(request,"login.html")

def login_load_post(request):
    user_name = request.POST['username']
    ps_word = request.POST['password']
    return render(request, 'login.html')

def  admin_Home(request):
    return render(request,"admin/admin_home.html")


def  admin_add_staff_load(request):
    return render(request,"admin/add-staff.html")

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
    staff_image = request.POST['image']
    return render(request, "admin/add-staff.html")


def admin_add_shedule_load(request):
    return render(request,"admin/add-shedule.html")

def admin_add_shedule_load_post(request):
    docname= request.POST['select']
    day = request.POST['date']
    f_rom = request.POST['from']
    to = request.POST['to']
    return render(request, "admin/add-shedule.html")


def admin_add_doctor_load(request):
    return render(request,"admin/adddoctor.html")

def admin_add_doctor_load_post(request):
    doc_name=request.POST['name']
    doc_place = request.POST['place']
    doc_pin = request.POST['pin']
    doc_post = request.POST['post']
    doc_department = request.POST['select']
    doc_gender = request.POST['fav_language']
    doc_experiense = request.POST['exp']
    doc_email = request.POST['email']
    doc_lisence = request.POST['file']
    doc_number = request.POST['no']
    doc_image = request.POST['image']
    return render(request, "admin/adddoctor.html")



def admin_add_dept_load(request):
    return render(request,"admin/amindadd-det.html")

def admin_add_dept_load_post(request):
    department = request.POST['username']
    textarea = request.POST['message']
    return render(request,"admin/amindadd-det.html")


def admin_adminviewdept_load(request):
    return render(request,"admin/Adminviewdept.html")

def admin_edit_dept(request):
    return render(request,"admin/edit-dept.html")

def admin_edit_staff(request):
    return render(request,"admin/edit-staff.html")


def admin_edit_doctor(request):
    return render(request,"admin/editdoctor.html")


def admin_edit_schedule(request):
    return render(request,"admin/edit-schedule.html")

def admin_leave_req(request):
    return render(request,"admin/leave-request.html")

def admin_view_attends(request):
    return render(request,"admin/view-attends.html")


def admin_view_doctor(request):
    return render(request,"admin/view-doctor.html")


def admin_view_shedule(request):
    return render(request,"admin/view-schedule.html")

def admin_view_staff(request):
    return render(request,"admin/viewstaff.html")

def admin_view_attends(request):
    return render(request,"admin/view-attends.html")






