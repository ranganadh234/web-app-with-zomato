from django.shortcuts import render
from pages.models import Pages
from django.core.paginator import Paginator
import requests

'''class SearchView(ListView):
    template_name='search/view.html'

    def get_context_data(self,*args,**kwargs):
        context=super(SearchView,self).get_context_data(*args,**kwargs)
        context['query']=self.request.GET.get('q')
        #SearchQuery.objects.create(query=context['query'])
        return context

    def get_queryset(self):
        request=self.request
        query=request.GET.get('q',None)
        if query is not None:
            return Pages.objects.search(query)
        return Pages.objects.all()'''

def search_view(request):
    print('request:',request)
    queryset=None
    #city_id
    if request.GET['city_id']:
        print('inside city_id')
        city_id=request.GET['city_id']
        if city_id:
            url="https://developers.zomato.com/api/v2.1/collections?city_id="+str(city_id)
            req=requests.get(url, headers = {"User-key": '1ec5908c1e671471d9bd924468eb41af'})
            queryset=req.json()#.items()

    #city_name
    if  request.GET['city_name']:
        print('inside city_name')
        city_name=request.GET['city_name']
        url="https://developers.zomato.com/api/v2.1/cities?q="+str(city_name)
        req=requests.get(url, headers = {"User-key": '1ec5908c1e671471d9bd924468eb41af'})
        city_id=req.json().get('location_suggestions').pop().get('id')#for getting first element we are using 0
        print('city_id:',city_id)
        if city_id:
            url="https://developers.zomato.com/api/v2.1/collections?city_id="+str(city_id)
            req=requests.get(url, headers = {"User-key": '1ec5908c1e671471d9bd924468eb41af'})
            queryset=None
            queryset=req.json()#.items()
            print('queryset:',queryset)
    #Pagination
    paginator=None
    paginator=Paginator(queryset['collections'],6)
    page=request.GET.get('page')
    paged_list=paginator.get_page(page)
    print('paged_list:',paged_list)
    context={
            "queryset":paged_list
    }
    #for obj in paged_list:
    #    print('obj:',obj['collection'].get('title'))
    return render(request,'pages/list.html',context)
