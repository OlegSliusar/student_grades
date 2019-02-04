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
    fStage = models.ForeignKey("Stage", default=None, on_delete=models.DO_NOTHING)
    department = models.ManyToManyField(Department)
    hint = models.TextField(max_length=300, null=True, blank=True, default=None)


class Grade(models.Model):
    class Meta:
        db_table = "grade"

    name = models.CharField(max_length=35)


class Stage(models.Model):
    class Meta:
        db_table = "stage"

    title = models.CharField(max_length=35)
    fSection = models.ForeignKey('Section', default=None, on_delete=models.DO_NOTHING)
