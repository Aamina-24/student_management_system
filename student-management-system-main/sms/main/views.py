from django.shortcuts import render, redirect
from .models import AboutPage, ContactPage, Student, Notice, Teacher, Feedback, LeaveRequest
from .forms import FeedbackForm, LeaveRequestForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    public_notices = Notice.objects.filter(isPublic=True)
    return render(request, 'home.html', {"public_notices": public_notices})

def about(request):
    about_text = AboutPage.objects.all()
    return render(request, 'about.html', {"aboutDetails": about_text})

def contact(request):
    contact_text = ContactPage.objects.all()
    return render(request, 'contact.html', {"contactDetails": contact_text})

def adminPanel(request):
    if 'admin_user' in request.session:
        all_students = Student.objects.all()
        all_teachers = Teacher.objects.all()
        return render(request, 'admin/admin_panel.html', {'students': all_students, 'teachers': all_teachers})
    else:
        return redirect('admin_login')

def adminLogin(request):
    if request.method == 'POST':
        admin_email = request.POST['email']
        admin_pwd = request.POST['pwd']
        if admin_email == "admin@gmail.com" and admin_pwd == "admin@123":
            request.session['admin_user'] = admin_email
            return redirect('admin_panel')
        else:
            return redirect('admin_login')
    return render(request, 'admin/admin_login.html')

def adminLogout(request):
    if 'admin_user' in request.session:
        del request.session['admin_user']
    return redirect('admin_login')

def adminAbout(request):
    about_details = AboutPage.objects.all()
    return render(request, 'admin/admin_about.html', {"aboutDetails": about_details})

def updateAbout(request, id):
    if request.method == 'POST':
        about_text = request.POST['text']
        about_obj = AboutPage.objects.get(id=id)
        about_obj.about = about_text
        about_obj.save()
    return redirect('admin_about')

def adminContact(request):
    contact_details = ContactPage.objects.all()
    return render(request, 'admin/admin_contact.html', {"contactDetails": contact_details})

def updateContact(request, id):
    if request.method == 'POST':
        contact_address = request.POST['address']
        contact_email = request.POST['email']
        contact_number = request.POST['contact']
        contact_obj = ContactPage.objects.get(id=id)
        contact_obj.address = contact_address
        contact_obj.email = contact_email
        contact_obj.contact_num = contact_number
        contact_obj.save()
    return redirect('admin_contact')

def addStudent(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        father_name = request.POST['f_name']
        mother_name = request.POST['m_name']
        gender = request.POST['gender']
        address = request.POST['address']
        city = request.POST['city']
        stu_email = request.POST['stu_email']
        contact_num = request.POST['contact_number']
        dob = request.POST['dob']
        course = request.POST['course']
        student_id = request.POST['stu_id']
        student_user_name = request.POST['stu_user_name']
        student_password = request.POST['stu_pwd']
        
        Student.objects.create(
            full_name=full_name, father_name=father_name, mother_name=mother_name,
            gender=gender, address=address, city=city, email=stu_email,
            contact_num=contact_num, date_of_birth=dob, course=course, stu_id=student_id,
            user_name=student_user_name, password=student_password
        )
    return render(request, 'admin/new_student.html')

def manageStudent(request):
    all_students = Student.objects.all()
    return render(request, 'admin/manage_students.html', {"students": all_students})

def updateStudent(request, id):
    if request.method == 'POST':
        student_obj = Student.objects.get(id=id)
        student_obj.full_name = request.POST.get('full_name', student_obj.full_name)
        student_obj.father_name = request.POST.get('f_name', student_obj.father_name)
        student_obj.mother_name = request.POST.get('m_name', student_obj.mother_name)
        student_obj.gender = request.POST.get('gender', student_obj.gender)
        student_obj.address = request.POST.get('address', student_obj.address)
        student_obj.city = request.POST.get('city', student_obj.city)
        student_obj.email = request.POST.get('stu_email', student_obj.email)
        student_obj.contact_num = request.POST.get('contact_number', student_obj.contact_num)
        student_obj.date_of_birth = request.POST.get('dob', student_obj.date_of_birth)
        student_obj.course = request.POST.get('course', student_obj.course)
        student_obj.stu_id = request.POST.get('stu_id', student_obj.stu_id)
        student_obj.user_name = request.POST.get('stu_user_name', student_obj.user_name)
        student_obj.password = request.POST.get('stu_pwd', student_obj.password)
        student_obj.save()
    return redirect('manage_students')

def deleteStudent(request, id):
    if 'admin_user' in request.session:
        Student.objects.get(id=id).delete()
    return redirect('manage_students')

def addNotice(request):
    if request.method == 'POST':
        notice_title = request.POST['notice_title']
        notice_content = request.POST['notice_content']
        is_public = request.POST['notice_status']
        Notice.objects.create(title=notice_title, content=notice_content, isPublic=is_public)
    return render(request, "admin/admin_notice.html")

def manageNotices(request):
    all_notices = Notice.objects.all()
    return render(request, 'admin/manage_notices.html', {'notices': all_notices})

def deleteNotice(request, id):
    if 'admin_user' in request.session:
        Notice.objects.get(id=id).delete()
    return redirect('manage_notices')

def updateNotice(request, id):
    if request.method == 'POST':
        notice_obj = Notice.objects.get(id=id)
        notice_obj.title = request.POST['title']
        notice_obj.content = request.POST['content']
        notice_obj.isPublic = request.POST['status']
        notice_obj.save()
    return redirect('manage_notices')

def addTeacher(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        gender = request.POST['gender']
        email = request.POST['email']
        contact_num = request.POST['contact_number']
        qualification = request.POST['qualification']
        
        Teacher.objects.create(
            full_name=full_name, gender=gender, email=email,
            contact_num=contact_num, qualification=qualification
        )
    return render(request, 'admin/add_teacher.html')

def manageTeachers(request):
    all_teachers = Teacher.objects.all()
    return render(request, 'admin/manage_teachers.html', {"teachers": all_teachers})

def deleteTeacher(request, id):
    Teacher.objects.get(id=id).delete()
    return redirect('manage_teachers')

def studentLogin(request):
    if 'student_user' not in request.session:
        if request.method == "POST":
            user_name = request.POST['userName']
            student_pwd = request.POST['stuPwd']
            if Student.objects.filter(user_name=user_name, password=student_pwd).exists():
                request.session['student_user'] = user_name
                return redirect('student_dashboard')
        return render(request, 'student/student_login.html')
    else:
        return redirect('student_dashboard')

def studentDashboard(request):
    if 'student_user' in request.session:
        student_in_session = Student.objects.get(user_name=request.session['student_user'])
        return render(request, 'student/student_dashboard.html', {"student": student_in_session})
    else:
        return redirect('student_login')

def studentLogout(request):
    if 'student_user' in request.session:
        del request.session['student_user']
    return redirect('student_login')

def updateFaculty(request, id):
    if request.method == 'POST':
        teacher_obj = Teacher.objects.get(id=id)
        teacher_obj.full_name = request.POST['full_name']
        teacher_obj.email = request.POST['email']
        teacher_obj.contact_num = request.POST['contact_number']
        teacher_obj.gender = request.POST['gender']
        teacher_obj.qualification = request.POST['qualification']
        teacher_obj.save()
    return redirect('manage_teachers')

def viewNotices(request):
    if 'student_user' in request.session:
        student_notice = Notice.objects.filter(isPublic=False)
        return render(request, 'student/view_notices.html', {"notices": student_notice})
    else:
        return redirect('student_login')

def studentSettings(request):
    if 'student_user' in request.session:
        student_obj = Student.objects.get(user_name=request.session['student_user'])
        if request.method == 'POST':
            current_pwd = request.POST['current_pwd']
            new_pwd = request.POST['new_pwd']
            if student_obj.password == current_pwd:
                student_obj.password = new_pwd
                student_obj.save()
                return redirect('student_dashboard')
        return render(request, "student/student_settings.html", {'student': student_obj})
    else:
        return redirect('student_login')

def submit_feedback(request):
    if 'student_user' in request.session:
        if request.method == 'POST':
            form = FeedbackForm(request.POST)
            if form.is_valid():
                feedback = form.save(commit=False)
                feedback.student = Student.objects.get(user_name=request.session['student_user'])
                feedback.save()
                return redirect('student_dashboard')  # Redirect to a success page
        else:
            form = FeedbackForm()
        return render(request, 'student/submit_feedback.html', {'form': form})
    else:
        return redirect('student_login')

def view_feedback(request):
    if 'admin_user' in request.session:
        feedback_list = Feedback.objects.all().order_by('-created_at')
        return render(request, 'admin/view_feedback.html', {'feedbacks': feedback_list})
    else:
        return redirect('admin_login')



@login_required
def apply(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.student = request.user
            leave_request.save()
            return redirect('leave_status')  # Redirect to a page showing the status of the leave request
    else:
        form = LeaveRequestForm()
    return render(request, 'student/apply_leave.html', {'form': form})
@login_required
def leave_status(request):
    leave_requests = LeaveRequest.objects.filter(student=request.user)
    return render(request, 'student/leave_status.html', {'leave_requests': leave_requests})

@login_required
def admin_manage_leaves(request):
    if not request.user.is_superuser:
        return redirect('student_dashboard')  # Redirect non-admin users
    
    leave_requests = LeaveRequest.objects.all()
    return render(request, 'admin/manage_leaves.html', {'leave_requests': leave_requests})

@login_required
def update_leave_status(request, id):
    if not request.user.is_superuser:
        return redirect('student_dashboard')  # Redirect non-admin users
    
    leave_request = LeaveRequest.objects.get(id=id)
    if request.method == 'POST':
        status = request.POST['status']
        leave_request.status = status
        leave_request.save()
        return redirect('admin_manage_leaves')
    return render(request, 'admin/update_leave_status.html', {'leave_request': leave_request})
