from collections import defaultdict

from io import TextIOWrapper
import io
from users.forms import *

from django.contrib import messages
from django.shortcuts import render, HttpResponse

from users.models import storetrafficdata
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
from django_pandas.io import read_frame





def adminlogin1(request):
    return render(request, "admin/adminlogin.html")

def adminloginentered(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        passwd=request.POST['upasswd']
        if uname =='admin' and passwd=='admin':
            return render(request,"admin/adminloginentered.html")
        else:
            return HttpResponse("invalied credentials")
    return render(request, "admin/adminloginentered.html")

def storecsvdata(request):
        if request.method == 'POST':
            #if request.method == "GET":
                #return render(request, template, prompt)
            csv_file = request.FILES['file']
            # let's check if it is a csv file
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'THIS IS NOT A CSV FILE')
            data_set = csv_file.read().decode('UTF-8')

            # setup a stream which is when we loop through each line we are able to handle a data in a stream
            io_string = io.StringIO(data_set)
            next(io_string)
            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                _, created = storetrafficdata.objects.update_or_create(
                    Date=column[1],
                    Day = column[2],
                    CodedDay = column[3],
                    Zone = column[4],
                    Weather = column[5],
                    Temperature = column[6],
                    Traffic = column[7]

                )
            context = {}

            '''
            name = request.POST.get('name')
            csvfile = TextIOWrapper(request.FILES['file'])
            # columns = defaultdict(list)
            storecsvdata=csv.DictReader(csvfile)

            for row1 in storecsvdata:
                Date = row1["Date"]
                Day = row1["Day"]
                CodedDay = row1["CodedDay"]
                Zone = row1["Zone"]
                Weather = row1["Weather"]
                Temperature = row1["Temperature"]
                Traffic = row1["Traffic"]


                storetrafficdata.objects.create(Date=Date, Day=Day, CodedDay=CodedDay,
                                              Zone=Zone, Weather=Weather, Temperature=Temperature,
                                              Traffic=Traffic)

            print("Name is ", csvfile)
            return HttpResponse('CSV file successful uploaded')
        else:
'''
        return render(request, 'admin/storecsvdata.html', {})




def userdetails(request):
    qs=userModel.objects.all()
    return render(request,"admin/userdetails.html",{"qs":qs})

def activateuser(request):
    if request.method =='GET':
        uname=request.GET.get('pid')
        print(uname)
        status='Activated'
        print("pid=",uname,"status=",status)
        userModel.objects.filter(id=uname).update(status=status)
        qs=userModel.objects.all()
        return render(request,"admin/userdetails.html",{"qs":qs})
