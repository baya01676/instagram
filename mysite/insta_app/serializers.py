from .models import (UserProfile, Post, PostLike, PostContent,
                     Follow, Favorite, FavoriteItem, Hashtag, Comment,
                     CommentLike,)
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username','password', 'first_name', 'phono_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class PostLikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = '__all__'


class FollowSerializers(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'


class PostContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostContent
        fields = '__all__'


class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class UserProfileListSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'username']


class UserProfileDetailSerializers(serializers.ModelSerializer):
    following = FollowSerializers(many=True, read_only=True)
    follower = FollowSerializers(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio', 'url_network', 'is_official', 'following', 'follower']


class PostListSerializers(serializers.ModelSerializer):
    post_comment = CommentSerializers(many=True, read_only=True)
    post_likes = PostLikeSerializers(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['music', 'hashtag', 'description', 'user', 'created_date', 'post_comment', 'post_likes']


class PostDetailSerializers(serializers.ModelSerializer):
    post_contents = PostContentSerializers(many=True, read_only=True)
    post_favorite = FavoriteSerializers(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['description', 'hashtag', 'created_date', 'music', 'post_contents', 'post_favorite']


class FavoriteItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'


class HashtagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'


class CommentLikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = '__all__'