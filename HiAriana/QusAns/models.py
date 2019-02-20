from django.db import models

class Statement(models.Model):
    Statement_text = models.CharField(max_length = 300)
    pub_datetime = models.DateField('date published')

class Answer(models.Model):
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 300)

