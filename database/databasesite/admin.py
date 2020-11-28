from django.contrib import admin
from .models import Employee, Department, Warehouse, Item, Project, Customer, Order

class EmployeeView(admin.ModelAdmin):
  list_display = ("number", "first_name", "last_name", "dnumber", "phone", "email")

class DepartmentView(admin.ModelAdmin):
  list_display = ("number", "name")

class WarehouseView(admin.ModelAdmin):
  list_display = ("number", "name", "location")

class ProjectView(admin.ModelAdmin):
  list_display = ("number", "name")

class ItemView(admin.ModelAdmin):
  list_display = ("number", "name","amount", "lot", "price", "warehouseNum")

class CustomerView(admin.ModelAdmin):
  list_display = ("id", "name", "projectNum")

class OrderView(admin.ModelAdmin):
  list_display = ("id", "item", "employee", "amount", "project", "datetime")

admin.site.register(Employee, EmployeeView)
admin.site.register(Department, DepartmentView)
admin.site.register(Warehouse, WarehouseView)
admin.site.register(Project, ProjectView)
admin.site.register(Item, ItemView)
admin.site.register(Customer, CustomerView)
admin.site.register(Order, OrderView)
