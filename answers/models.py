from django.db import models


class Answer(models.Model):
    class Meta:
        db_table = "answer"

    fUser = models.ForeignKey("users.User", default=None, on_delete=models.CASCADE)

    fQuestion = models.ForeignKey("my_site.Question", on_delete=models.DO_NOTHING)
    answer_like = models.BooleanField()
    fGrade = models.ForeignKey('my_site.Grade', on_delete=models.DO_NOTHING)

class Review(models.Model):
    class Meta:
        db_table = "review"
    fAnswer = models.ForeignKey("Answer", on_delete=models.DO_NOTHING)
    fGrade = models.ForeignKey("my_site.Grade", on_delete=models.DO_NOTHING)
    comment = models.TextField()
    fUserExpert = models.ForeignKey("users.User", default=None, on_delete=models.CASCADE)

