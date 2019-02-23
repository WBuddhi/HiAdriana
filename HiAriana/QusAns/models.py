from django.db import models

class QA_JFile(models.Model):
    QA_File = models.CharField(max_length = 10000)
    pub_datetime = models.DateTimeField('Timestamp', auto_now_add=True)


class Statement(models.Model):
    qa_jfile = models.ForeignKey(QA_JFile, on_delete=models.CASCADE)
    Statement_text = models.CharField(max_length = 300)
    pub_datetime = models.DateTimeField('Timestamp', auto_now_add=True)

class Answer(models.Model):
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 300)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


