from django.db import models

class Department(models.Model):
  number = models.CharField(max_length=2, primary_key=True)
  name = models.CharField(max_length=30)
  def __str__(self):
    return self.name

class Employee(models.Model):
  number = models.CharField(max_length=10, primary_key=True)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  dnumber = models.ForeignKey(Department, on_delete=models.CASCADE)
  def __str__(self):
    return self.first_name + " " + self.last_name

class Warehouse(models.Model):
  number = models.CharField(max_length=5, primary_key=True)
  name = models.CharField(max_length=30)
  location = models.CharField(max_length=30)
  def __str__(self):
    return self.name

class Lott(models.Model):
  number = models.CharField(max_length=10, primary_key=True)
  date = models.DateField(auto_now_add=True)
  warehouse_number = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
  def __str__(self):
    return self.number

class Customer(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  name = models.CharField(max_length=30)
  def __str__(self):
    return self.name

class Item(models.Model):
  number = models.CharField(max_length=10, primary_key=True)
  name = models.CharField(max_length=30)
  lott = models.ForeignKey(Lott, on_delete=models.CASCADE)
  def __str__(self):
    return self.name

class Order(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  amount = models.IntegerField()
  def __str__(self):
    return self.id