

from django.urls import path
from django.conf.urls import include, url
#from django.views.generic import ListView, DetaiView
from django.views.generic import ListView, DetailView
from news.models import Articles


urlpatterns = [

    path(r'', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
                                 template_name="news/posts.html"))
]
