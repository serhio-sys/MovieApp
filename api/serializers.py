from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
    
    class Meta:
        model = Movie
        fields = ('id', 'title', 'image', 'description', 'genres','released','raiting')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('author', 'movie', 'text')


class UserSerializer(serializers.ModelSerializer):
    #favorite = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), many=True)
    favorite = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'favorite')