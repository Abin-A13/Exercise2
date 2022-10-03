from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import User



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8,write_only=True)


    def create(self, validated_data):
        email = validated_data['email']
        pwd = validated_data['password']
        role = validated_data['role']
        usr = validated_data['username']
        user_obj = User.objects.create_user(email=email,password=pwd,role=role,username=usr)
        return user_obj

    class Meta:
        model = User
        fields = ['id', 'email','username','password', 'role']