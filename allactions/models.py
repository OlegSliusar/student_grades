from django.db import models

class Department(models.Model):
    class Meta:
        db_table = "department"
    name = models.CharField(max_length=35)

class Section(models.Model):
    class Meta:
        db_table = "section"
    name = models.CharField(max_length=35)

class Question(models.Model):
    class Meta:
        db_table = "question"
    title = models.CharField(max_length=35)
    fStep = models.ForeignKey("my_site.Stage", default=None, on_delete=models.DO_NOTHING)

class Grade(models.Model):
    class Meta:
        db_table = "grade"
    name = models.CharField(max_length=35)
