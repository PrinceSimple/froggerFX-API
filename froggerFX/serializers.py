from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from froggerFX.models import Player

# Player Object Serializer
class PlayerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Player
    fields = '__all__'
  
  """ def update(self, instance, validated_data):
    user_data = validated_data.pop('user')
    username = self.data['user']['username']
    user = User.objects.get(username=username)
    user_serializer = UserSerializer(data=user_data)
    if user_serializer.is_valid():
        user_serializer.update(user, user_data)
    instance.save()
    return instance """

# User Serializer
class UserSerializer(serializers.ModelSerializer):
  player = PlayerSerializer()
  class Meta:
    model = User
    fields = ('id', 'username', 'player')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('username', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_user(validated_data['username'], "",  validated_data['password'])
    return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")