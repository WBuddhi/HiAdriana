from django.db import models

class Statement(models.Model):
    Statement_text = models.CharField(max_length = 300)
    pub_datetime = models.DateField('date published', auto_now_add=True)

class Answer(models.Model):
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 300)


class QusJsonFile(models.Model):
    TimeStamp = models.DateField('date uploaded', auto_now_add=True)
    document = models.FileField(upload_to = 'Qusfiles/')