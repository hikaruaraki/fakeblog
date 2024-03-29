from django.db import models
from django.utils import timezone

class Postmodels(models.Model):
    title = models.CharField(verbose_name='タイトル',max_length=100)
    media = models.ImageField(verbose_name='画像',upload_to='photo',blank=True, null=True)
    post = models.CharField(verbose_name='内容',max_length=1000)
    published_date = models.DateTimeField(verbose_name='投稿日時',blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Commentmodels(models.Model):
    users = models.CharField(default='名無し',max_length=100)
    comment = models.CharField(verbose_name='内容',max_length=500)
    publishe_date = models.DateTimeField(verbose_name='投稿日時',blank=True, null=True)

    def publish(self):
        self.publishe_date = timezone.now()
        self.save()