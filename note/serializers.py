from rest_framework import serializers
from django.contrib.auth.models import User
from note.models import Note

class NoteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    model=User
    fields='__all__'

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
