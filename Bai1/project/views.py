from django.shortcuts import render
from .models import pro


# Create your views here.
def list(request):
    Data = {'Pro': pro.objects.all().order_by('language')}
    return render(request, 'projects.html', Data)

def detail(request, id):
    pr = pro.objects.get(id=id)
    data = {'Pro': pr}
    return render(request, 'projectDetails.html', data)

