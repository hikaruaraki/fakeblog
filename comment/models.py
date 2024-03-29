from django.db import models
from django.utils import timezone

class Commentmodels(models.Model):
    users = models.CharField(verbose_name='ユーザ名',max_length=100)
    comment = models.CharField(verbose_name='内容',max_length=500)
    publishe_date = models.DateTimeField(verbose_name='投稿日時',blank=True, null=True)

    def publish(self):
        self.publishe_date = timezone.now()
        self.save()