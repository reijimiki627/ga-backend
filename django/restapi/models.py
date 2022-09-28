from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_name = models.CharField(verbose_name='ユーザ名',max_length=32)
    created_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True) 