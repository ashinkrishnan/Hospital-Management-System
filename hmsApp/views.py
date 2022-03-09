
from django.shortcuts import render,redirect
from django.contrib import messages
from django.template import context
from .models import *
from django.contrib.auth.models import User, Group

from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse

from django.utils import timezone

# Create your views here.

def home(request):
    return render(request,'index.html')

def loginUser(request):
    if request.method =='POST':
            username_email = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username_email, password=password)
            

            if user is not None:
                login(request,user)
                grp=request.user.groups.all()[0].name
                if grp == 'Patient':
                    context ={}
                    return render(request,'profile_home.html', context)
                elif grp == 'Cardiodoctor':
                    context={}
                    return render(request, 'doctorprofile.html', context)
                elif grp == 'Orthodoctor':
                    context={}
                    return render(request, 'doctorprofile.html', context)
                elif grp == 'Pulmonologydoctor':
                    context={}
                    return render(request, 'doctorprofile.html', context)
                elif grp == 'Urologydoctor':
                    context={}
                    return render(request, 'doctorprofile.html', context)
                         

            else:
                messages.error(request, 'Incorrect Username or Password ...')
    
    context={}
    return render(request,'login.html',context)

def registerUser(request):
    if request.method == 'POST' :
        username = request.POST['username']
        email = request.POST['email']
        contactnumber=request.POST['contactnumber']
        password = request.POST['password']
        Repeatpassword = request.POST['password1']

        if password == Repeatpassword:

            
            if Patient.objects.filter(email=email).exists():
                messages.info(request, 'email taken..try another ...!')
                return redirect('register')
            else:
                Patient.objects.create(username=username, email=email, contactnumber=contactnumber)
                user=User.objects.create_user(first_name=username, email=email, password=password, username=email)

                pat_group = Group.objects.get(name='Patient')
                pat_group.user_set.add(user)

                user.save()
                
                
        else:
            messages.info(request, 'password not matching .. re-enter password')
            return redirect('register')

        return redirect('login')

    else:
        
        context={}
        return render(request,'registration.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/')

def userProfile(request):
    if not request.user.is_active :
        return redirect('login')
    else:
        grp = request.user.groups.all()[0].name
        print(grp)

        if grp == 'Patient':
             return render(request,'profile_home.html')
        elif grp == 'Cardiodoctor':
            return render(request, 'doctorprofile.html')
        elif grp == 'Orthodoctor':
            return render(request, 'doctorprofile.html')
        elif grp == 'Pulmonologydoctor':
            return render(request, 'doctorprofile.html')
        elif grp == 'Urologydoctor':
            return render(request, 'doctorprofile.html')

def profileDetails(request):
    if not request.user.is_active :
        return redirect('login')

    grp = request.user.groups.all()[0].name
    print(grp)

    if grp == 'Patient':

        patient_details = Patient.objects.all().filter(email=request.user)
        context={'patient_details':patient_details}
        return render(request,'profile_details.html',context)

    elif grp == 'Cardiodoctor':
        
        
        doctor_details = CardioDoc.objects.all().filter(email=request.user)
        context={'doctor_details':doctor_details}
        
        return render(request,'doctorprofile_details.html',context)
    elif grp == 'Orthodoctor':
        
        
        doctor_details = OrthoDoc.objects.all().filter(email=request.user)
        context={'doctor_details':doctor_details}
        
        return render(request,'doctorprofile_details.html',context)

    elif grp == 'Pulmonologydoctor':
        
        
        doctor_details = PulmonoDoc.objects.all().filter(email=request.user)
        context={'doctor_details':doctor_details}
        
        return render(request,'doctorprofile_details.html',context)

    elif grp == 'Urologydoctor':
        
        
        doctor_details = UroDoc.objects.all().filter(email=request.user)
        context={'doctor_details':doctor_details}
        
        return render(request,'doctorprofile_details.html',context)






def cardioDocs(request):
    if not request.user.is_active:
        return redirect('login')

    all_docs = CardioDoc.objects.all()
    context = {'all_docs':all_docs}

    return render(request,'docList_cardio.html',context)

def orthoDocs(request):
    if not request.user.is_active:
        return redirect('login')

    all_docs = OrthoDoc.objects.all()
    context={'all_docs':all_docs}
    return render(request, 'docList_ortho.html', context)

def pulmonoDocs(request):
    if not request.user.is_active:
        return redirect('login')

    all_docs = PulmonoDoc.objects.all()
    context={'all_docs':all_docs}
    return render(request, 'docList_pulmono.html', context)

def uroDocs(request):
    if not request.user.is_active:
        return redirect('login')

    all_docs = UroDoc.objects.all()
    context={'all_docs':all_docs}
    return render(request, 'docList_uro.html', context)


def cardioAppointment(request):
    if not request.user.is_active:
        return redirect('login')

    error=""
    
    all_docs = CardioDoc.objects.all()
    context = {'all_docs':all_docs}

    if request.method == 'POST':
        temp = request.POST['doctorname']

        
        
        doctorname = temp.split()[0]
        doctormail = temp.split()[1]

        patientname = request.POST['patientname']
        patientemail= request.POST['patientemail']
        appointmentdate=request.POST['appointmentdate']
        appointmenttime= request.POST['appointmentime']
        symptoms=request.POST['symptoms']

        try:
            Appointment.objects.create(doctorname=doctorname, doctormail=doctormail, patientname=patientname, 
            patientmail=patientemail, appointmentdate=appointmentdate, appointmenttime=appointmenttime,
            symptoms=symptoms,prescription="", status=True)

            error="no"
        except Exception as e:
            # raise e
            error="yes"

        e={'error':error}
        return render(request, 'appointment_cardio.html', e )

    return render(request,'appointment_cardio.html',context)

def orthoAppointment(request):
    if not request.user.is_active:
        return redirect('login')

    error=""
    
    all_docs = OrthoDoc.objects.all()
    context = {'all_docs':all_docs}

    if request.method == 'POST':
        temp = request.POST['doctorname']

        
        
        doctorname = temp.split()[0]
        doctormail = temp.split()[1]

        patientname = request.POST['patientname']
        patientemail= request.POST['patientemail']
        appointmentdate=request.POST['appointmentdate']
        appointmenttime= request.POST['appointmentime']
        symptoms=request.POST['symptoms']

        try:
            Appointment.objects.create(doctorname=doctorname, doctormail=doctormail, patientname=patientname, 
            patientmail=patientemail, appointmentdate=appointmentdate, appointmenttime=appointmenttime,
            symptoms=symptoms,prescription="", status=True)

            error="no"
        except Exception as e:
            # raise e
            error="yes"

        e={'error':error}
        return render(request, 'appointment_ortho.html', e )

    return render(request,'appointment_ortho.html',context)

def pulmonoAppointment(request):
    if not request.user.is_active:
        return redirect('login')

    error=""
    
    all_docs = PulmonoDoc.objects.all()
    context = {'all_docs':all_docs}

    if request.method == 'POST':
        temp = request.POST['doctorname']

        
        
        doctorname = temp.split()[0]
        doctormail = temp.split()[1]

        patientname = request.POST['patientname']
        patientemail= request.POST['patientemail']
        appointmentdate=request.POST['appointmentdate']
        appointmenttime= request.POST['appointmentime']
        symptoms=request.POST['symptoms']

        try:
            Appointment.objects.create(doctorname=doctorname, doctormail=doctormail, patientname=patientname, 
            patientmail=patientemail, appointmentdate=appointmentdate, appointmenttime=appointmenttime,
            symptoms=symptoms,prescription="", status=True)

            error="no"
        except Exception as e:
            # raise e
            error="yes"

        e={'error':error}
        return render(request, 'appointment_pulmono.html', e )

    return render(request,'appointment_pulmono.html',context)

def uroAppointment(request):
    if not request.user.is_active:
        return redirect('login')

    error=""
    
    all_docs = UroDoc.objects.all()
    context = {'all_docs':all_docs}

    if request.method == 'POST':
        temp = request.POST['doctorname']

        
        
        doctorname = temp.split()[0]
        doctormail = temp.split()[1]

        patientname = request.POST['patientname']
        patientemail= request.POST['patientemail']
        appointmentdate=request.POST['appointmentdate']
        appointmenttime= request.POST['appointmentime']
        symptoms=request.POST['symptoms']

        try:
            Appointment.objects.create(doctorname=doctorname, doctormail=doctormail, patientname=patientname, 
            patientmail=patientemail, appointmentdate=appointmentdate, appointmenttime=appointmenttime,
            symptoms=symptoms,prescription="", status=True)

            error="no"
        except Exception as e:
            # raise e
            error="yes"

        e={'error':error}
        return render(request, 'appointment_uro.html', e )

    return render(request,'appointment_uro.html',context)


def viewAppointments(request):
    if not request.user.is_active:
        return render('login')
    g = request.user.groups.all()[0].name
    if g == 'Patient':
        upcoming_appointments = Appointment.objects.filter(patientmail=request.user, appointmentdate__gte=timezone.now(),status=True).order_by('appointmentdate')
        previous_appointments = Appointment.objects.filter(patientmail=request.user, appointmentdate__lt=timezone.now()).order_by('-appointmentdate')| Appointment.objects.filter(patientmail=request.user, status=False).order_by('-appointmentdate')
        context={'upcoming_appointments':upcoming_appointments, 'previous_appointments':previous_appointments}

        return render(request,'patient_appointmentview.html', context)
    
    elif g == 'Cardiodoctor':
        print(g)
        if request.method == 'POST':
            prescription_data = request.POST['prescription']
            id_value = request.POST['idofappointment']
            Appointment.objects.filter(id=id_value).update(prescription=prescription_data, status=False)
        upcoming_appointments = Appointment.objects.filter(doctormail=request.user, appointmentdate__gte=timezone.now(),status=True).order_by('appointmentdate')
        previous_appointments = Appointment.objects.filter(doctormail=request.user, appointmentdate__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(doctormail=request.user, status=False).order_by('-appointmentdate')
        context={'upcoming_appointments':upcoming_appointments, 'previous_appointments':previous_appointments}

        print(upcoming_appointments)

        return render(request,'doctorappointmentview.html', context)

    elif g == 'Orthodoctor':
        print(g)
        if request.method == 'POST':
            prescription_data = request.POST['prescription']
            id_value = request.POST['idofappointment']
            Appointment.objects.filter(id=id_value).update(prescription=prescription_data, status=False)
        upcoming_appointments = Appointment.objects.filter(doctormail=request.user, appointmentdate__gte=timezone.now(),status=True).order_by('appointmentdate')
        previous_appointments = Appointment.objects.filter(doctormail=request.user, appointmentdate__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(doctormail=request.user, status=False).order_by('-appointmentdate')
        context={'upcoming_appointments':upcoming_appointments, 'previous_appointments':previous_appointments}

        print(upcoming_appointments)

        return render(request,'doctorappointmentview.html', context)

    elif g == 'Pulmonologydoctor':
        print(g)
        if request.method == 'POST':
            prescription_data = request.POST['prescription']
            id_value = request.POST['idofappointment']
            Appointment.objects.filter(id=id_value).update(prescription=prescription_data, status=False)
        upcoming_appointments = Appointment.objects.filter(doctormail=request.user, appointmentdate__gte=timezone.now(),status=True).order_by('appointmentdate')
        previous_appointments = Appointment.objects.filter(doctormail=request.user, appointmentdate__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(doctormail=request.user, status=False).order_by('-appointmentdate')
        context={'upcoming_appointments':upcoming_appointments, 'previous_appointments':previous_appointments}

        print(upcoming_appointments)

        return render(request,'doctorappointmentview.html', context)

    elif g == 'Urologydoctor':
        print(g)
        if request.method == 'POST':
            prescription_data = request.POST['prescription']
            id_value = request.POST['idofappointment']
            Appointment.objects.filter(id=id_value).update(prescription=prescription_data, status=False)
        upcoming_appointments = Appointment.objects.filter(doctormail=request.user, appointmentdate__gte=timezone.now(),status=True).order_by('appointmentdate')
        previous_appointments = Appointment.objects.filter(doctormail=request.user, appointmentdate__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(doctormail=request.user, status=False).order_by('-appointmentdate')
        context={'upcoming_appointments':upcoming_appointments, 'previous_appointments':previous_appointments}

        print(upcoming_appointments)

        return render(request,'doctorappointmentview.html', context)


    





    


       

    


