from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Pages
import requests

def page_list_view(request):
    '''url="https://developers.zomato.com/api/v2.1/collections?city_id=6"
    req=requests.get(url, headers = {"User-key": '1ec5908c1e671471d9bd924468eb41af'})
    queryset=req.json()#.items()
    #print(queryset)
    paginator=Paginator(queryset['collections'],6)
    page=request.GET.get('page')
    paged_list=paginator.get_page(page)
    print('paged_list:',paged_list)
    context={
            "queryset":paged_list
    }
    for obj in paged_list:
        print('obj:',obj['collection'].get('title'))'''
    return render(request,'pages/list.html')#,context)

def index(request):
    return render(request,'pages/index.html')
