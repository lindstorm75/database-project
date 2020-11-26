from django.db import models

class Department(models.Model):
  department_number = models.CharField(max_length=2, primary_key=True)
  department_name = models.CharField(max_length=30)
  def __str__(self):
    return self.department_name

class Employee(models.Model):
  employee_number = models.CharField(max_length=10, primary_key=True)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  dnumber = models.ForeignKey(Department, on_delete=models.CASCADE)
  def __str__(self):
    return self.first_name + " " + self.last_name

class Warehouse(models.Model):
  warehouse_number = models.CharField(max_length=5, primary_key=True)
  name = models.CharField(max_length=30)
  location = models.CharField(max_length=30)
  def __str__(self):
    return self.name

class Lott(models.Model):
  lott_number = models.CharField(max_length=10, primary_key=True)
  date = models.DateField(auto_now_add=True)
  warehouse_number = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
  def __str__(self):
    return self.lott_number

class Item(models.Model):
  item_number = models.CharField(max_length=10, primary_key=True)
  name = models.CharField(max_length=30)
  lott = models.ForeignKey(Lott, on_delete=models.CASCADE)
  def __str__(self):
    return self.name

class Customer(models.Model):
  customer_id = models.CharField(max_length=10, primary_key=True)
  name = models.CharField(max_length=30)
  def __str__(self):
    return self.name

class Order(models.Model):
  order_id = models.CharField(max_length=10, primary_key=True)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  amount = models.IntegerField()
  def __str__(self):
    return self.order_id