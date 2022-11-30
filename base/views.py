from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.


def index(request):
    
    if request.method == 'POST':
        link = request.POST.get('link')
        uid = str(uuid.uuid4())[0:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid) 

    return render(request, 'index.html')

