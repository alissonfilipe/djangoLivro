from django.urls.conf import include
from django.contrib import admin
from django.urls import path

urlpatterns = [

    path('',include('website.urls',namespace='website'))

    #INTERFACE ADMINISTRATIVA
    path('admin/', admin.site.urls),
]
