from django.contrib.auth import get_user_model
from rest_framework import serializers
from main.models import message
from main.models import UserProfile, message, User
import django_filters.rest_framework


# # 抱枕序列号 bao_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
# # 用户-子女 id owner_id = models.CharField(max_length=16)
# # 密码 password = models.CharField(max_length=64)
# # 地址 palce = models.CharField(max_length=64)
# # 主人1 年龄 human1_age = models.IntegerField()
# # 主人1 身体状况 human1_status = models.CharField(max_length=64)
# # 主人2 年龄 human2_age = models.IntegerField()
# # 主人2 身体状况 human2_status = models.CharField(max_length=64)
# # ip ip = models.CharField(max_length=64)

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         # fields = '__all__'
#         fields = ('User','bao_id', 'human1_age', 'human1_status', 'human2_age', 'human2_status', 'ip')
class UserProfile_Message(serializers.RelatedField):
    def to_representation(self, value):
        return '%s' % value.User.username


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url', 'bao_id', 'UserProfile_Message', 'palce', 'human_age', 'human_status', 'human_xue', 'human_sex')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = message
        # fields = '__all__'
        fields = ('User', 'type', 'time', 'content')

class MessageSerializer(serializers.HyperlinkedModelSerializer):

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    class Meta:
        model = message
        fields = ('User','type', 'time', 'content')


class Message_Detail_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = message
        fields = ('User', 'type', 'time', 'content')

UserModel = get_user_model()


# - 注册
# User = models.OneToOneField('auth.User', unique=True, verbose_name='用户信息', on_delete=models.CASCADE)
# # 抱枕序列号
# bao_id = models.CharField(max_length=16)
# # 地址
# palce = models.CharField(max_length=64)
#
# # 主人1 个人信息
# human = models.IntegerField()
# human_status = models.CharField(max_length=64)
# human_xue = models.IntegerField()
# human_sex = models.CharField(max_length=10)
class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    bao_id = serializers.CharField(write_only=True)
    human_age = serializers.IntegerField(write_only=True)
    human_status = serializers.CharField(write_only=True)
    human_xue = serializers.CharField(write_only=True)
    human_sex = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'bao_id', 'human_age', 'human_status', 'human_xue', 'human_sex')

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
        )
        bao_id = validated_data['bao_id']
        human_age = validated_data['human_age']
        human_status = validated_data['human_status']
        human_xue = validated_data['human_xue']
        human_sex = validated_data['human_sex']
        user.set_password(validated_data['password'])
        UserProfile.objects.create(User=user, bao_id=bao_id, human_age=human_age, human_status=human_status,
                                   human_sex=human_sex, human_xue=human_xue)
        user.save()
        return user
