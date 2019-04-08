
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('webexample/', include('webexample.urls')),
    path('', include('mainApp.urls')),
]
