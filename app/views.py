from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def create_student(request):
    ESTFO=StudentForm()
    d={'ESTFO':ESTFO}

    if request.method=='POST':
        STFDO=StudentForm(request.POST)
        if STFDO.is_valid():
            sid=STFDO.cleaned_data['sid']
            sname=STFDO.cleaned_data['sname']
            sage=STFDO.cleaned_data['sage']
            email=STFDO.cleaned_data['email']
            SO=Student.objects.get_or_create(sid=sid,sname=sname,sage=sage,email=email)[0]
            SO.save()
            return HttpResponse('Student Details created successfully')
        else:
            return HttpResponse('Invalid Data')

    return render(request,'create_student.html',d)