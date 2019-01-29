from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    class Meta:
        db_table = "role"
    name = models.CharField(max_length=35)

class Grade(models.Model):
    class Meta:
        db_table = "grade"
    name = models.CharField(max_length=35)

class Department(models.Model):
    class Meta:
        db_table = "department"
    name = models.CharField(max_length=35)

class Permission(models.Model):
    class Meta:
        db_table = "permission"
    code_name = models.CharField(max_length=35)

class Step(models.Model):
    class Meta:
        db_table = "step"
    title = models.CharField(max_length=35)
    fSection = models.ForeignKey('Section', on_delete=models.DO_NOTHING)

class Section(models.Model):
    class Meta:
        db_table = "section"
    name = models.CharField(max_length=35)

class Answer(models.Model):
    class Meta:
        db_table = "answer"

    fUser = models.ForeignKey("users.User", default=None, on_delete=models.CASCADE)

    fQuestion = models.ForeignKey("Question", on_delete=models.DO_NOTHING)
    answer_like = models.BooleanField()
    fGrade = models.ForeignKey('Grade', on_delete=models.DO_NOTHING)

class Question(models.Model):
    class Meta:
        db_table = "question"
    title = models.CharField(max_length=35)
    fStep = models.ForeignKey("Step", on_delete=models.DO_NOTHING)

class ExpertReview(models.Model):
    class Meta:
        db_table = "expert_review"
    fAnswer = models.ForeignKey("Answer", on_delete=models.DO_NOTHING)
    fGrade = models.ForeignKey("Grade", on_delete=models.DO_NOTHING)
    comment = models.TextField()
    fUserExpert = models.ForeignKey("users.User", on_delete=models.CASCADE)
