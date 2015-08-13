from django.shortcuts import render

from .models import DateAndTime

def home(request):
    dateAndTime = DateAndTime()
    dateAndTime.save()

    dateAndTimes = DateAndTime.objects.all()
    return render(request, 'home.html', {'dateAndTimes': dateAndTimes})

