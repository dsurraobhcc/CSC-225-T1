import requests
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    # return render(request, "index.html")
    r = requests.get('http://httpbin.org/status/418')
    
    output = r.text + '\r\n' + str(datetime.now())
    output += '\r\n !!!!!!'

    return HttpResponse('<pre>' + output + '</pre>')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
