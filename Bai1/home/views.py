from django.shortcuts import render
from project.models import pro
from .forms import RegistrationForm
from django.http import HttpResponseRedirect


def index(request):
    Data = {'Pro': pro.objects.all().order_by('language')}
    return render(request, 'pages/home.html', Data)


def projects(request):
    return render(request, 'pages/projects.html')


def information(request):
    return render(request, 'pages/information.html')


def contact(request):
    return render(request, 'pages/contact.html')

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})