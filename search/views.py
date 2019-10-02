from django.shortcuts import render
from pages.models import Pages
from django.core.paginator import Paginator
import requests


def search_view(request):
    #city_id
    global queryset
    if request.GET.get('city_id',False):
        city_id=request.GET.get('city_id',False)
        if city_id:
            url="https://developers.zomato.com/api/v2.1/collections?city_id="+str(city_id)
            req=requests.get(url, headers = {"User-key": '1ec5908c1e671471d9bd924468eb41af'})
            queryset=req.json()

    #city_name
    if  request.GET.get('city_name',False):
        city_name=request.GET.get('city_name',False)
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
    context={
            "queryset":paged_list
    }
    return render(request,'pages/list.html',context)
