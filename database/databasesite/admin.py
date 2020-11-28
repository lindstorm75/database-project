from django.contrib import admin
from .models import Employee, Department, Warehouse, Item, Project, Customer, Order

class EmployeeView(admin.ModelAdmin):
  list_display = ("id", "first_name", "last_name", "location", "phone", "email", "department_id")

class DepartmentView(admin.ModelAdmin):
  list_display = ("id", "name")

class WarehouseView(admin.ModelAdmin):
  list_display = ("id", "name", "location")

class ProjectView(admin.ModelAdmin):
  list_display = ("id", "name")

class ItemView(admin.ModelAdmin):
  list_display = ("id", "name",  "price", "amount", "lott_id", "warehouse_id")

class CustomerView(admin.ModelAdmin):
  list_display = ("id", "name")

class OrderView(admin.ModelAdmin):
  list_display = ("id", "item_id", "employee_id", "amount", "datetime")

admin.site.register(Employee, EmployeeView)
admin.site.register(Department, DepartmentView)
admin.site.register(Warehouse, WarehouseView)
admin.site.register(Project, ProjectView)
admin.site.register(Item, ItemView)
admin.site.register(Customer, CustomerView)
admin.site.register(Order, OrderView)
