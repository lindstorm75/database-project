from django.db import models

class Department(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=30)
  def __str__(self):
    return f"{self.id}"

class Employee(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  location = models.CharField(max_length=32)
  phone = models.CharField(max_length=10)
  email = models.EmailField(null=False)
  department_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="employee")
  def __str__(self):
    return self.id

class Warehouse(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=30)
  location = models.CharField(max_length=30)
  def __str__(self):
    return f"{self.id}"

class Customer(models.Model):
  id = models.CharField(max_length=12, primary_key=True)
  name = models.CharField(max_length=30)
  def __str__(self):
    return self.id

class Item(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=30)
  amount = models.IntegerField()
  lott_id = models.IntegerField()
  warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name="item")
  price = models.IntegerField()
  def __str__(self):
    return f"{self.id}"

class Project(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=30) 
  employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="item")
  customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="item")
  def __str__(self):
    return f"{self.id}"

class Order(models.Model):
  id = models.AutoField(primary_key=True)
  item_id = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_order")
  employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="emp_order")
  project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="proj_order")
  amount = models.IntegerField(null=False)
  datetime = models.DateTimeField()
  def __str__(self):
    return f"{self.id}"