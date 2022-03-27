from django.db import models


class Leave_Types(models.Model):
    leave_type = models.CharField(max_length=45)
    leave_days = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.leave_type
