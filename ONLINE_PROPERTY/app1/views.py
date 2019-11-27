from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from .models import NewPlotReg,APPARTmentCReg,Sales,Employee,User
# Create your views here.
def showloginhtml(request):

    return render(request,"login.html")


def welcomeuser(request):
    uname = request.POST.get("username")
    pword = request.POST.get("password")

    if uname== "admin" and pword == "admin":
        return render(request,"welcomepage.html")
    else:
        return render(request,"login.html",{"message":"Please Enter Valid Userid or Password"})


class ViewNewPlotReg(CreateView):
    model = NewPlotReg
    fields = "__all__"
    template_name = "newplotreg.html"
    success_url = "/plotadded/"


class UpdatePlot(UpdateView):
    model = NewPlotReg
    fields = ["cost_per_sq_yard","other_expences","status","total_cost"]
    template_name = "updateplot.html"
    success_url = "/plotadded/"


class ViewPlot(ListView):
    model = NewPlotReg
    template_name = "listview.html"


class GetUpdateNo(ListView):
    model = NewPlotReg
    template_name = "getupdateno.html"


class Appartment(CreateView):
    model = APPARTmentCReg
    fields = "__all__"
    template_name = "newappartmntreg.html"
    success_url = "/welcomepage/"


class ViewAppartment(ListView):
    model = APPARTmentCReg
    template_name = "listappartment.html"


class CreateSALES(CreateView):
    model = Sales
    fields = "__all__"
    template_name = "createsales.html"
    success_url = "/welcomepage/"


class Viewsales(ListView):
    model = Sales
    template_name = "listsales.html"


class ViewsalesFordelete(ListView):
    model = Sales
    template_name = "viewsalesfordelete.html"


class DeleteconfirmSales(DeleteView):
    model = Sales
    template_name ="successdeletesales.html"
    success_url = "/welcomepage/"

class SoldPlot(ListView):
    model = NewPlotReg
    template_name = "soldplot.html"

class ReservedPlot(ListView):
    model = NewPlotReg
    template_name = "reservedplot.html"

class VacantPlot(ListView):
    model = NewPlotReg
    template_name = "vacantplot.html"

class AddEmployee(CreateView):
    model = Employee
    fields = "__all__"
    template_name = "addemployee.html"
    success_url = "/welcomepage/"

class ViewEmployee(ListView):
    model = Employee
    template_name = "viewemployee.html"


class AddUser(CreateView):
    model = User
    fields = "__all__"
    template_name = "createuser.html"
    success_url = "/welcomepage/"


class ViewUser(ListView):
    model = User
    template_name = "listviewuser.html"


class UpdateUser(UpdateView):
    model = User
    fields = ["user_name","user_password"]
    template_name = "updateuser.html"
    success_url = "/welcomepage/"


class DeleteUser(DeleteView):
    model = User
    template_name = "deleteuser.html"
    success_url = "/welcomepage/"


class DELETEforVIEWuser(ListView):
    model = User
    template_name = "deleteforviewuser.html"