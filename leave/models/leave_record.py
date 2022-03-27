from django.db import models
from employees.models import Employee


class LeaveRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_year = models.IntegerField()
    entitlement = models.IntegerField(default=21)
    residue = models.IntegerField(default=0)
    leave_applied = models.IntegerField(default=0)
    total_taken = models.IntegerField(default=0)

    class Meta:
        unique_together = ("employee", "leave_year")

    def __str__(self):
        return f"Leave Record {self.leave_year}"

    @property
    def balance(self):
        return (self.entitlement + self.residue) - self.total_taken
