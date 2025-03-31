"""traffic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as users
from traffic import views as traffic

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', users.index, name='index'),
    path('logout/',users.logout,name='logout'),
    path('userlogin/',users.userlogin,name='userlogin'),
    path('userregister/',users.userregister,name='userregister'),
    path('userlogincheck/',users.userlogincheck,name='userlogincheck'),
    path('randomforest/', users.randomforest, name='randomforest'),
    path('svm/', users.svm, name='svm'),
    path('adddata/', users.adddata, name='adddata'),


    path('adminlogin1/',traffic.adminlogin1,name='adminlogin1'),
    path('adminloginentered/',traffic.adminloginentered,name='adminloginentered'),
    path('storecsvdata/',traffic.storecsvdata,name='storecsvdata'),
    path('userdetails/',traffic.userdetails,name='userdetails'),
    path('activateuser/',traffic.activateuser,name='activateuser'),


]
