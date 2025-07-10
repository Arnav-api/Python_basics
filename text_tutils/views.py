import re
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'Name': 'Arnav' , 'Place':'Lucknow'}
    return render(request, 'index.html',params)

def personal(Request):
    return HttpResponse(" Name: Arnav Khandelwal<br>Age:19<br>Interest: Python<br>Current Proficiency in Django: Beginner")

def Django_learn(Request):
    return HttpResponse(''' Link to study Django<br><br> <a href='https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7'> Django Playlist for Begineer</a> ''')

def Machine_Learning(Request):
    return HttpResponse(''' Access to Machine Learning tutorial is down below<br><br> <a href="https://www.youtube.com/watch?v=gmvvaobm7eQ&list=PLeo1K3hjS3uvCeTYTeyfe0-rN5r8zn9rw" > ML Playlist </a> ''')

def Functionality(Request):
    return HttpResponse(''' Based on User Descrition : <br> <a href='/' > <br>Go To Home </a><br><br> <a href='/personal' > Developer Description <a/>''')

def Transform_Sentences(Request):
    b=Request.GET.get('text','default')
    option=Request.GET.get('User Details','off')
    if option == 'on':
        pattern = 'name is ([a-zA-z ]*) ' 
        _name_=re.findall(pattern,b)
        pattern2='from ([a-zA-z ]*) city'
        _city_=re.findall(pattern2,b)
        pattern3='student in ([a-zA-Z ]*)'
        _study_=re.findall(pattern3,b)
        return HttpResponse(f"Following can be extracted about the user:<br>{_name_}<br>{_city_}<br>{_study_}")
    else:
        return HttpResponse("Error")
def remove_punctuations(Request):
    a= Request.GET.get('removepunc','off')
    c= Request.GET.get('text','No Input')
    if a =='on':
        punctuations= '''.,!#"':;?/'''
        edited_text=""
        for i in c:
            if i not in punctuations:
                edited_text=edited_text+i
                
        params={'purpose':a,'action':edited_text}
        return render(Request,'analyze.html',params)
    else:
        return HttpResponse("Error")

    