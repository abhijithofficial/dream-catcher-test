from rest_framework import serializers
from user.models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    firstname = serializers.CharField(min_length=3)
    lastname = serializers.CharField(min_length=3)
    address = serializers.CharField(min_length=3)
    phone = serializers.CharField(min_length=10)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'], first_name=validated_data['firstname'],
                                        last_name=validated_data['lastname'],
                                        address=validated_data['address'],
                                        phonenumber=validated_data['phone']
                                        )
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email',
                  'password', 'firstname', 'lastname', 'address', 'phone')


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',
                  'first_name', 'last_name', 'address', 'phonenumber')
