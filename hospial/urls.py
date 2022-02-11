"""hspapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = (
    path("login_load/", views.login_load),
    path("login_load_post", views.login_load_post),
    path("admin_add_shedule_load/", views.admin_add_shedule_load),
    path("admin_add_shedule_load_post/", views.admin_add_shedule_load_post),
    path("admin_add_doctor_load/", views.admin_add_doctor_load),
    path("admin_add_doctor_load_post/", views.admin_add_doctor_load_post),
    path("admin_add_staff_load/", views.admin_add_staff_load),
    path("admin_add_staff_load_post/", views.admin_add_staff_load_post),
    path("admin_add_dept_load/", views.admin_add_dept_load),
    path("admin_add_dept_post/", views.admin_add_dept_post),
    path("admin_adminviewdept_load/", views.admin_adminviewdept_load),
    path("admin_edit_dept/<depid>", views.admin_edit_dept),
    path("admin_update_dept/", views.admin_update_dept),
    path("admin_edit_staff/<sid>", views.admin_edit_staff),
    path("admin_update_staff/", views.admin_update_staff),
    path("admin_edit_doctor/<did>", views.admin_edit_doctor),
    path("admin_update_doctor/", views.admin_update_doctor),
    path("admin_edit_schedule/<sch>", views.admin_edit_schedule),
    path("admin_update_schedule/", views.admin_update_schedule),
    path("admin_leave_req/", views.admin_leave_req),
    path("admin_view_attends/", views.admin_view_attends),
    path("admin_view_doctor/", views.admin_view_doctor),
    path("admin_view_shedule/<docid>", views.admin_view_shedule),
    path("admin_view_staff/", views.admin_view_staff),
    path("admin_view_attends/", views.admin_view_attends),
    path("admin_home/", views.admin_Home),
    path("admin_delect_dept/<deptid>", views.admin_delect_dept),
    path("admin_delect_doctor/<docid>", views.admin_delect_doctor),
    path("admin_delect_schedule/<scheduleid>", views.admin_delect_schedule),
    path("admin_delect_staff/<staffid>", views.admin_delect_staff),
    path("admin_view_serach/", views.admin_view_serach),
    path("admin_view_doc_serach/", views.admin_view__doc_serach),
    path("admin_view_staff_serach/", views.admin_view__staff_serach),
    path("admin_schedule_search/", views.admin_schedule_search),
    path("adminviewdoctorschedule/<id>", views.adminviewdoctorschedule),
    path("admin_add_user_load/", views.admin_add_user_load),
    path("admin_user_load_post/", views.admin_user_load_post),
    path("bookingSchedule/",views.bookingSchedule)
)
