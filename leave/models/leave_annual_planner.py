from django.db import models

from employees.models import Employee
from leave.models.leave_types import Leave_Types


class annual_planner(models.Model):
    leave_year = models.CharField(max_length=5)
    leave_month = models.CharField(max_length=4, default='Jan')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave = models.ForeignKey(Leave_Types, on_delete=models.CASCADE, default=1)
    date_from = models.DateField()
    date_to = models.DateField()
    no_of_days = models.IntegerField(default=0)
    status = models.CharField(max_length=15, default='Pending')