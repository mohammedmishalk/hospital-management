from django.shortcuts import render

# Create your views here.

def login_load(request):
    return render(request,"login.html")

def  admin_Home(request):
    return render(request,"admin/admin_home.html")


def  admin_add_staff_load(request):
    return render(request,"admin/add-staff.html")


def admin_add_shedule_load(request):
    return render(request,"admin/add-shedule.html")

def admin_add_doctor_load(request):
    return render(request,"admin/adddoctor.html")

def admin_add_dept_load(request):
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






