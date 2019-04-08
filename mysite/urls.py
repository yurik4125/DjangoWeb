
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'webexample/', include('webexample.urls')),
    path(r'', include('mainApp.urls')),
    path(r'news/', include('news.urls'))
]
