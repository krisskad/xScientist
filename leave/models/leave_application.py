from django.db import models

from employees.models import Employee
from leave.models.leave_types import Leave_Types
from organisation_details.models import Department, Team


class LeaveApplication(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="Employees")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(Leave_Types, on_delete=models.CASCADE)
    apply_date = models.DateField(auto_now=True)
    start_date = models.DateField()
    end_date = models.DateField()
    no_of_days = models.PositiveIntegerField()
    supervisor = models.ForeignKey(Employee, on_delete=models.CASCADE,
                                   related_name="Supervisor", blank=True, null=True)
    supervisor_status = models.CharField(max_length=15, default="Pending")
    supervisor_comment = models.TextField(blank=True, null=True, default="None")
    hod = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="hod",
                            blank=True, null=True)
    hod_status = models.CharField(max_length=15, default="Pending")
    hod_comment = models.TextField(blank=True, null=True, default="None")
    hr = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="hr",
                           blank=True, null=True)
    hr_status = models.CharField(max_length=15, default="Pending")
    hr_comment = models.TextField(blank=True, null=True, default="None")
    overall_status = models.CharField(max_length=10, default="Pending")
    remarks = models.TextField(default="None")
    balance = models.IntegerField(default=0)
    expired = models.BooleanField(default=False)

    def __str__(self):
        return f"{id} - {self.leave_type} - {self.employee.first_name}"