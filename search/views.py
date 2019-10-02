from django.shortcuts import render
from pages.models import Pages
from django.core.paginator import Paginator
import requests


def search_view(request):
    #city_id
    if request.GET['city_id']:
        print('inside city_id')
        city_id=request.GET['city_id']
        if city_id:
            url="https://developers.zomato.com/api/v2.1/collections?city_id="+str(city_id)
            req=requests.get(url, headers = {"User-key": '1ec5908c1e671471d9bd924468eb41af'})
            queryset=req.json()

    #city_name
    if  request.GET['city_name']:
        city_name=request.GET['city_name']
        url="https://developers.zomato.com/api/v2.1/cities?q="+str(city_name)
        req=requests.get(url, headers = {"User-key": '1ec5908c1e671471d9bd924468eb41af'})
        city_id=req.json().get('location_suggestions').pop().get('id')#for getting first element we are using 0
        if city_id:
            url="https://developers.zomato.com/api/v2.1/collections?city_id="+str(city_id)
            req=requests.get(url, headers = {"User-key": '1ec5908c1e671471d9bd924468eb41af'})
            queryset=req.json()
    #Pagination
    paginator=Paginator(queryset['collections'],6)
    page=request.GET.get('page')
    paged_list=paginator.get_page(page)
    print('paged_list:',paged_list)
    context={
            "queryset":paged_list
    }
    return render(request,'pages/list.html',context)
