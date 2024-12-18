from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser, Student, LibraryHistory, FeesHistory

#serializer for user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']
        read_only_fields = ['id']

#serializer for user registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'password', 'confirm_password']
        extra_kwargs = {
            'email': {'required': True},
            'role': {'required': True}
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
#serializer for loging in for a user
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError('Unable to login with provided credentials.')
        else:
            raise serializers.ValidationError('Must include "username" and "password".')
        
        data['user'] = user
        return data

#serializer for students
class StudentSerializer(serializers.ModelSerializer):
    library_records = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    fees_records = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Student
        fields = '__all__'

#serializer for library use
class LibraryHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryHistory
        fields = '__all__'

#serializer for all fee records
class FeesHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeesHistory
        fields = '__all__'