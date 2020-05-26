from django.db import models

# Create your models here.
# login/models.py

class User(models.Model):
    '''用户表'''
    gender = (
        (0, 'personnel'),
        (1, 'Admin'),
    )
    name = models.CharField(verbose_name="用户名", max_length=128, unique=True)  # unique表示唯一
    password = models.CharField(verbose_name="密码", max_length=256)
    user_type = models.IntegerField(verbose_name="用户类型", choices=gender, default=0)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # 用于将django自带管理员端汉化
    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = verbose_name