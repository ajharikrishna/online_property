"""ONLINE_PROPERTY URL Configuration

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
from django.views.generic import TemplateView
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showloginhtml),
    path('savepassword/',views.welcomeuser),
    path('newplot/',views.ViewNewPlotReg.as_view()),
    path('plotadded/',TemplateView.as_view(template_name="plotadded.html")),
    path('welcomepage/',TemplateView.as_view(template_name="welcomepage.html")),

    path('updateplot1<int:pk>/',views.UpdatePlot.as_view()),
    path('viewplot/',views.ViewPlot.as_view()),
    path('updateplot/',views.GetUpdateNo.as_view()),
    path('createappartment/',views.Appartment.as_view()),
    path('viewappartment/',views.ViewAppartment.as_view()),
    path('createsales/',views.CreateSALES.as_view()),
    path('viewsales/',views.Viewsales.as_view()),
    path('deletesales/',views.ViewsalesFordelete.as_view()),
    path('deleteconfirmsales<int:pk>/',views.DeleteconfirmSales.as_view()),
    path('soldplots/',views.SoldPlot.as_view()),
    path('reservedplots/',views.ReservedPlot.as_view()),
    path('vacantplots/',views.VacantPlot.as_view()),
    path('addemployee/',views.AddEmployee.as_view()),
    path('viewemployee/',views.ViewEmployee.as_view()),
    path('about/',TemplateView.as_view(template_name="about.html")),
    path('logout/',views.showloginhtml),
    path('adduser/',views.AddUser.as_view()),
    path('viewuser/',views.ViewUser.as_view()),
    path('updateuser<int:pk>/',views.UpdateUser.as_view()),
    path('deleteuser1<int:pk>/',views.DeleteUser.as_view()),
    path('deleteuser/',views.DELETEforVIEWuser.as_view())





]
