import uuid

from django.db import models


# Create your models here.
# 1.用户表（主键id 抱枕序列号 用户-子女id 密码 地址 主人1年龄  身体1状况 主人2年龄 主人 身体2状况 ip）

class User(models.Model):
    # 抱枕序列号
    bao_id = models.CharField(max_length=16)
    # 用户-子女 id
    owner_id = models.CharField(max_length=16)
    # 密码
    password = models.CharField(max_length=64)
    # 地址
    palce = models.CharField(max_length=64)
    # 主人1 年龄
    human1_age = models.IntegerField()
    # 主人1 身体状况
    human1_status = models.CharField(max_length=64)
    # 主人2 年龄
    human2_age = models.IntegerField()
    # 主人2 身体状况
    human2_status = models.CharField(max_length=64)
    # ip
    ip = models.CharField(max_length=64)


# 2.消息记录（主键id  外键:用户表主键id 提醒类别 提醒时间 提醒内容)
class message(models.Model):
    User = models.ForeignKey('User',on_delete=models.CASCADE)
    type = models.CharField(max_length=64)
    time = models.DateTimeField()
    content = models.CharField(max_length=64)

