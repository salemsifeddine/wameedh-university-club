from django.shortcuts import render
from .models import *
# Create your views here.


def main(request):
    members=Members.objects.all()
    achievements=ClubAchivement.objects.all()
    events=ClubEvents.objects.all()
    aboutus=AboutUsInfo.objects.all()

    context={"members":members,"achievements":achievements,"events":events,"aboutus":aboutus}

    return render(request, "pages/main.html",context)

def earth(request):
    context={}
    return render(request, "pages/index.html",context)