from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.loginUser,name='login'),
    path('register/',views.registerUser,name='register'),
    path('logout/',views.logoutUser,name='logout'),

    path('HomeProfile/',views.userProfile,name='HomeProfile'),
    path('ProfileDetails/', views.profileDetails, name='ProfileDetails'),

    path('cardioDocs/',views.cardioDocs, name='cardioDocs'),
    path('cardioAppointment/',views.cardioAppointment, name='cardioAppointment'),

    path('patientAppointmentview/', views.viewAppointments, name='patientAppointmentview'),

    path('orthoDocs/',views.orthoDocs, name='orthoDocs'),
    path('orthoAppointment/',views.orthoAppointment, name='orthoAppointment'),

    path('pulmomoDocs/',views.pulmonoDocs, name='pulmonoDocs'),
    path('pulmonoAppointment/',views.pulmonoAppointment, name='pulmonoAppointment'),

    path('uroDocs/',views.uroDocs, name='uroDocs'),
    path('uroAppointment/',views.uroAppointment, name='uroAppointment')

    
]