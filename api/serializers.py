from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Post, Comment, User, Follow, Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
                        slug_field='username', 
                        read_only=True, 
                        default=serializers.CurrentUserDefault()
                        )
    following = serializers.SlugRelatedField(
                            slug_field='username', 
                            queryset=User.objects.all()
                            )

    def validate(self, data):
        if data.get('following') == self.context['request'].user:
            raise serializers.ValidationError("Please enter full name") 
        return data

    class Meta:
        fields = '__all__'  
        model = Follow
