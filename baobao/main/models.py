import uuid

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# 1.用户表（主键id 抱枕序列号 用户-子女id 密码 地址 主人1年龄  身体1状况 主人2年龄 主人 身体2状况 ip）

class UserProfile(models.Model):
    # 用户 - 子女id 密码
    User = models.OneToOneField('auth.User', unique=True, verbose_name='用户信息', on_delete=models.CASCADE)
    # 抱枕序列号
    bao_id = models.CharField(max_length=16)
    # 地址
    palce = models.CharField(max_length=64)

    # 主人1 个人信息
    human = models.IntegerField()
    human_status = models.CharField(max_length=64)
    human_xue = models.IntegerField()
    human_sex = models.CharField(max_length=10)


# 2.消息记录（主键id  外键:用户表主键id 提醒类别 提醒时间 提醒内容)
class message(models.Model):
    User = models.ForeignKey('main.UserProfile', on_delete=models.CASCADE)
    type = models.CharField(max_length=64)
    time = models.DateTimeField()
    content = models.CharField(max_length=64)
