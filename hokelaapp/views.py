from django.shortcuts import get_object_or_404, render, redirect
from django.http  import HttpResponse, HttpResponseRedirect
# from hokelaapp.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime as dt
from .models import Excel
from tablib import Dataset
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
    return render(request, 'index.html')