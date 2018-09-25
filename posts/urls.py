from django.conf.urls import url
from django.urls import path, re_path
from . import views # from . means from all

urlpatterns = [
    url('', views.index, name='index'),
    re_path(r'details/(?P<id>\d+)/$', views.details, name='details')
]
