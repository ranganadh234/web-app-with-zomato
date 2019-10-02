from django.urls import path
from .views import page_list_view,index
urlpatterns=[
            path('list/',page_list_view,name='page-list'),
            path('',index,name='index'),

]
