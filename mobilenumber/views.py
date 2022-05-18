from cgitb import html
from importlib.resources import contents
from itertools import count
from multiprocessing import context
from tempfile import tempdir
from urllib import request
from webbrowser import get
from xml.etree.ElementTree import Comment
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import phonemodel, reviewmodel
from django.db.models import Count
# Create your views here.
def index(request):
    allnumbers = phonemodel.objects.all()
    reviews= reviewmodel.objects.all()
    count= reviews.count()
    list_of_reviews=[]
    i=0
    for review in reviews:
        review_no= review.reviewnumber.phone_number
        if not any(d['review_number'] == review_no  for d in list_of_reviews):
            temp_no= {'review_number': review_no, 'count': i}
            list_of_reviews.append(temp_no)
            i=0
        else:
            i= i+1
            pass
           

    print('list:::::::', list_of_reviews)    

        # print('review_no:::::::', review_no)
    print('count::::::::::', count)
   
    context={'allnumbers': allnumbers}
    return render(request, 'mobilenumber/home.html', context)
def search(request):
    number= request.GET.get('number', None)
    review_text = request.GET.get("review_text", None)
    review_number = request.GET.get("number_review", None)
    review_status = request.GET.get("reviewstatus", None)
    alluser= phonemodel.objects.filter(phone_number=number)
    print(alluser)
    if review_text:
        numbers_forigen_key = phonemodel.objects.filter(phone_number=review_number)
        number_fk = numbers_forigen_key[0]
        review = reviewmodel.objects.create(reviewnumber = number_fk, review = review_text, review_status=review_status )
        review.save()
        alluser= phonemodel.objects.filter(phone_number=review_number)
        return redirect('/')

    if alluser.exists():
        alluser = alluser[0]
    else:
        number = "+"+number  
        number = number.replace(" ", '')
        alluser= phonemodel.objects.filter(phone_number=number)
        if alluser.exists():
            alluser = alluser[0]  
        
    print(alluser)
    context= {'alluser': alluser}
    
    return render(request, 'mobilenumber/search.html', context)
def reportnumber(request):
    reportednumber= request.GET.get('phone',None)
    reportedstatus= request.GET.get('reportedstatus',None)
    reportedcomment=request.GET.get('reportedcomment',None)
    print(reportednumber, type(reportnumber))
    context = {}
    if reportednumber:
        if phonemodel.objects.filter(phone_number= reportednumber):
            messages.success(request, 'This number is already reported, you can search and add your review')
        else:    
            reports = phonemodel.objects.create(phone_number = reportednumber, comment=reportedcomment, status= reportedstatus)
            reports.save()
            messages.success(request, 'You have succesfully reported the number')
        
    return render(request, 'mobilenumber/reportnumber.html', context=context)

def allnumbers(request):
    allnumbers = phonemodel.objects.all()
    
    context={'allnumbers': allnumbers}
    return render(request,'mobilenumber/allnumbers.html', context )
def numberview(request, number_id):
    one_number= phonemodel.objects.get(id)
    print(id)
    context= {'one_number': one_number}
    return render(request, 'mobilenumber/numbers.html', context)

