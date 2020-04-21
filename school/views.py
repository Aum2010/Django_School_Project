from django.shortcuts import render , redirect
from django.http import HttpResponse #เขียนบนกระดาษ
from .models import ExamScore
from django.contrib.auth.models import User
# Create your views here.

def HomePage(request):
    # return HttpResponse('<h1>Django</h1>')
    return render(request,'school/block.html')

def AboutPage(request):
    return render(request,'school/about.html')

def ContactPage(request):
    return render(request,'school/contact.html')

def ScorePage(request):
    score = ExamScore.objects.all()

    context = {'score' : score}

    return render(request,'school/score.html' , context)


def RegisterPage(request):
    if request.method == 'POST':
       data = request.POST.copy()
       name = data.get('name')
       name_last = data.get('name_last')
       email = data.get('email')
       password = data.get('password')

       newuser = User()
       newuser.username = email
       newuser.first_name = name
       newuser.last_name = name_last
       newuser.email = email
       newuser.set_password(password)
       newuser.save()
       return redirect('home-page')

    return render(request,'school/register.html')