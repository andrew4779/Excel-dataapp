from django.shortcuts import get_object_or_404, render, redirect
from django.http  import HttpResponse, HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime as dt
# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')
