from django.db import models

class Department(models.Model):
  number = models.CharField(max_length=2, primary_key=True)
  name = models.CharField(max_length=30)
  def __str__(self):
    return f"{self.number}:{self.name}"

class Employee(models.Model):
  number = models.CharField(max_length=10, primary_key=True)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  location = models.CharField(max_length=32)
  phone = models.CharField(max_length=10)
  email = models.EmailField()
  dnumber = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="employee")
  def __str__(self):
    return f"{self.number}:{self.first_name} {self.last_name}"

class Warehouse(models.Model):
  number = models.CharField(max_length=5, primary_key=True)
  name = models.CharField(max_length=30)
  location = models.CharField(max_length=30)
  def __str__(self):
    return f"{self.number}:{self.name}"

class Project(models.Model):
  number = models.CharField(max_length=5, primary_key=True)
  name = models.CharField(max_length=30)
  def __str__(self):
    return f"{self.number}:{self.name}"

class Customer(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  name = models.CharField(max_length=30)
  projectNum = models.ForeignKey(Project, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.id}:{self.name}"

class Item(models.Model):
  number = models.CharField(max_length=10, primary_key=True)
  name = models.CharField(max_length=30)
  amount = models.IntegerField()
  lot = models.IntegerField()
  warehouseNum = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name="item")
  price = models.IntegerField()
  def __str__(self):
    return f"{self.number}: {self.name} lot:{self.lot}"

class Order(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_order")
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="emp_order")
  project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="proj_order")
  amount = models.IntegerField()
  datetime = models.DateTimeField()
  def __str__(self):
    return f"{self.id}"