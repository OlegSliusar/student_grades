from django.db import models

class Department(models.Model):
    class Meta:
        db_table = "department"
    name = models.CharField(max_length=35)
