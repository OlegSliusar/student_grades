from django.conf import settings
from django.db import models
# from django.contrib.auth.models import User



class Stage(models.Model):
    class Meta:
        db_table = "stage"
    title = models.CharField(max_length=35)
    fSection = models.ForeignKey('allactions.Section', default=None, on_delete=models.DO_NOTHING)
