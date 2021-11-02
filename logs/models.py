from django.db import models
from django.contrib.auth.models import User
from employee.models import Employee


# Create your models here.
class Logs(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="logs_employee", null=True, blank=True)
    action = models.TextField(max_length=10000)
    action_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="logs_user")
    action_date = models.DateField()