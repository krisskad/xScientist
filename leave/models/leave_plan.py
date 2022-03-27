from django.db import models

from employees.models import Employee
from leave.services import get_number_of_days_without_public_holidays


class LeavePlan(models.Model):
    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'
    EXPIRED = 'Expired'

    APPROVAL_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (EXPIRED, 'Expired')
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    plan_date = models.DateField(auto_now=True)
    description = models.TextField(blank=True)
    expired = models.BooleanField(default=False)
    approval_status = models.CharField(
        max_length=8,
        choices=APPROVAL_CHOICES,
        default=PENDING,
    )

    @property
    def no_of_days(self):
        return get_number_of_days_without_public_holidays(self.start_date, self.end_date)
