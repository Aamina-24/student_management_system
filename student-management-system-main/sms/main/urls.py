from django.urls import path
from . import views

urlpatterns = [
    # Public views
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Admin views
    path('admin/', views.adminPanel, name='admin_panel'),
    path('admin/login/', views.adminLogin, name='admin_login'),
    path('admin/logout/', views.adminLogout, name='admin_logout'),
    path('admin/about/', views.adminAbout, name='admin_about'),
    path('admin/about/update/<int:id>/', views.updateAbout, name='update_about'),
    path('admin/contact/', views.adminContact, name='admin_contact'),
    path('admin/contact/update/<int:id>/', views.updateContact, name='update_contact'),
    path('admin/students/add/', views.addStudent, name='add_student'),
    path('admin/students/manage/', views.manageStudent, name='manage_students'),
    path('admin/students/update/<int:id>/', views.updateStudent, name='update_student'),
    path('admin/students/delete/<int:id>/', views.deleteStudent, name='delete_student'),
    path('admin/notices/add/', views.addNotice, name='add_notice'),
    path('admin/notices/manage/', views.manageNotices, name='manage_notices'),
    path('admin/notices/delete/<int:id>/', views.deleteNotice, name='delete_notice'),
    path('admin/notices/update/<int:id>/', views.updateNotice, name='update_notice'),
    path('admin/teachers/add/', views.addTeacher, name='add_teacher'),
    path('admin/teachers/manage/', views.manageTeachers, name='manage_teachers'),
    path('admin/teachers/delete/<int:id>/', views.deleteTeacher, name='delete_teacher'),
    path('admin/teachers/update/<int:id>/', views.updateFaculty, name='update_faculty'),
    path('admin/feedback/', views.view_feedback, name='view_feedback'),

    # Student views
    path('student/login/', views.studentLogin, name='student_login'),
    path('student/dashboard/', views.studentDashboard, name='student_dashboard'),
    path('student/logout/', views.studentLogout, name='student_logout'),
    path('student/notices/', views.viewNotices, name='view_notices'),
    path('student/settings/', views.studentSettings, name='student_settings'),
    path('student/feedback/', views.submit_feedback, name='submit_feedback'),

   

    # Student URLs
    path('student/apply/', views.apply, name='apply'),
    path('student/leave-status/', views.leave_status, name='leave_status'),

    # Admin URLs
    path('admin/manage-leaves/', views.admin_manage_leaves, name='admin_manage_leaves'),
    path('admin/update-leave-status/<int:id>/', views.update_leave_status, name='update_leave_status'),
]

