from django.utils.translation import gettext as _
from rest_framework import serializers

from .models import User, StudentProfile


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'full_name',
            'date_joined',
            'user_type',
            'is_active',
            'is_staff',
            'is_superuser',
        )

        read_only_fields = ('email', 'is_staff', 'is_superuser', 'date_joined')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = (
            'github_profile',
            'linkedin_profile',
            'major'
        )


class StudentRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
            'password2',
            'profile',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(_('Passwords are not the same!'))
        data = super().validate(attrs)
        data.pop('password2')
        return data

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')

        user = User.objects.create_user(**validated_data, user_type=User.STUDENT_TYPE)

        StudentProfile.objects.create(**profile_data)

        return user
