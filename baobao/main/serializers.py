from django.contrib.auth import get_user_model
from rest_framework import serializers
from main.models import message
from main.models import User, message


# # 抱枕序列号 bao_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
# # 用户-子女 id owner_id = models.CharField(max_length=16)
# # 密码 password = models.CharField(max_length=64)
# # 地址 palce = models.CharField(max_length=64)
# # 主人1 年龄 human1_age = models.IntegerField()
# # 主人1 身体状况 human1_status = models.CharField(max_length=64)
# # 主人2 年龄 human2_age = models.IntegerField()
# # 主人2 身体状况 human2_status = models.CharField(max_length=64)
# # ip ip = models.CharField(max_length=64)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('User','bao_id', 'human1_age', 'human1_status', 'human2_age', 'human2_status', 'ip')



# User = models.ForeignKey('User',on_delete=models.CASCADE)
# type = models.CharField(max_length=64)
# time = models.DateTimeField()
# content = models.CharField(max_length=64)
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = message
        # fields = '__all__'
        fields = ('User', 'type', 'time', 'content')


UserModel = get_user_model()
#  注册绑定
class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'password')
    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        User.objects.create(User=user)
        user.save()
        return user