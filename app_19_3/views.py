from django.shortcuts import render

# Create your views here.
from .models import *

def home(request):
    personal_info = PersonalInfo.objects.first()
    qualifications = Qualification.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    return render(request, 'home.html', {
        'personal_info': personal_info,
        'qualifications': qualifications,
        'skills': skills,
        'projects': projects,
        
    })
def contact(request):
    return render(request,'contact.html')
def certificates_view(request):
    certificates = Certificate.objects.all()
    return render(request, 'certificates.html', {'certificates': certificates})

