from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Bookings

def bookings(request):
    if request.method == 'POST':
        fullname=request.POST.get('fullname',False)
        datetime=request.POST.get('datetime',False)
        guests=request.POST.get('guests',False)
        obj=Bookings(fullname=fullname,datetime=datetime,guests=guests)
        obj.save()
        if obj is not None:
            return redirect('search')
        else:
            return redirect('slots')
    else:
        return render(request,'bookings/bookings_form.html')
