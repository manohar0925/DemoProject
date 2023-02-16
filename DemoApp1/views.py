from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def f1(manu):
    return HttpResponse('<h1> HELLO USER GOOD AFTERNOON***</H1><HR/><BR/>')
def f2(manu):
    return HttpResponse('<h2> NAMASTE GURUGARU🌚</H2><HR/>')
