from django.http import HttpResponse
from django.shortcuts import render
from . models import team
# Create your views here.
def index(request):
    obj=team.objects.all()
    return render(request,'index.html',{'members':obj})