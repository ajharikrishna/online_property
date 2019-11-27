from django.db import models

class NewPlotReg(models.Model):
    plot_no = models.IntegerField(primary_key=True)
    road_no = models.IntegerField()
    plot_area_in_sq_yard = models.CharField(max_length=30)
    surveyno = models.IntegerField()
    cost_per_sq_yard = models.DecimalField(max_digits=10,decimal_places=2)
    other_expences = models.DecimalField(max_digits=10,decimal_places=2)
    boundaries = models.CharField(max_length=30)
    facing = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    total_cost = models.DecimalField(max_digits=10,decimal_places=2)


class APPARTmentCReg(models.Model):
    app_no = models.IntegerField(primary_key=True)
    app_floors = models.IntegerField()
    app_status = models.CharField(max_length=30)
    app_area = models.CharField(max_length=30)
    app_cost = models.DecimalField(max_digits=10,decimal_places=2)

class Sales(models.Model):
    sales_id_no = models.IntegerField(primary_key=True)
    plot_sales_rs = models.IntegerField()
    appartment_sales_rs = models.IntegerField()
    total_sales_rs = models.IntegerField()

class Employee(models.Model):
    employee_id_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    salary = models.DecimalField(max_digits=10,decimal_places=2)

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name =models.CharField(max_length=30)
    user_password = models.CharField(max_length=10)