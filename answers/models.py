from django.db import models


class Answer(models.Model):
    class Meta:
        db_table = "answer"

    fUser = models.ForeignKey("users.User", default=None, on_delete=models.CASCADE)

    fQuestion = models.ForeignKey("allactions.Question", default=None, on_delete=models.DO_NOTHING)
    answer_like = models.BooleanField()
    fGrade = models.ForeignKey('allactions.Grade', default=None, on_delete=models.DO_NOTHING)

class Review(models.Model):
    class Meta:
        db_table = "review"
    fAnswer = models.ForeignKey("Answer", on_delete=models.DO_NOTHING)
    fGrade = models.ForeignKey("allactions.Grade", null=True, on_delete=models.DO_NOTHING)
    comment = models.TextField()
    fUserExpert = models.ForeignKey("users.User", default=None, on_delete=models.CASCADE)
