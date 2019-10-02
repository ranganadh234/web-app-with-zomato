from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Pages
import requests

def page_list_view(request):
    return render(request,'pages/list.html')

def index(request):
    return render(request,'pages/index.html')
