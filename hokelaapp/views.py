from django.shortcuts import get_object_or_404, render, redirect
from django.http  import HttpResponse, HttpResponseRedirect
# from hokelaapp.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime as dt
from .models import Excel
from tablib import Dataset
from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Excel
from tablib import Dataset
# from.serializer import ExcelSerializer
import io, csv
from .forms import *
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import permission_required,login_required
import os
from django.conf import settings
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# from .resources import ExcelResource
# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def excel_upload(request):
    if request.method == 'POST':
        # excel_resource = ExcelResource()
        dataset = Dataset()
        new_excel = request.FILES["myfile"]
        if not new_excel.name.endswith('.xlsx'):
            messages.error(request,'this is not a .xlsx file')
            return render(request,'index.html')
        imported_data = dataset.load(new_excel.read(),format='xlsx')
        for data in imported_data:
            value = Excel(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9]
                )
            value.save()
    return render(request, 'home.html')