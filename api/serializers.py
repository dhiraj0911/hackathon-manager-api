from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Hackathon, HackathonParticipant, Submission

class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = '__all__'

class HackathonParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = HackathonParticipant
        fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']