from django.shortcuts import render
from app27.mymiddleware import showDate

def showIndex(request):
    return render(request,"index.html",{"c_date":showDate()})