from django.shortcuts import get_object_or_404 
from rest_framework import viewsets, status, filters
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
 
from .models import Post, Comment, Group, Follow, User
from .serializers import CommentSerializer, PostSerializer, GroupSerializer, FollowSerializer
 

class PostViewSet(viewsets.ModelViewSet): 
    queryset = Post.objects.all() 
    serializer_class = PostSerializer 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group',]  
     
    def perform_create(self, serializer): 
        serializer.save(author=self.request.user) 
 
	 
class CommentViewSet(viewsets.ModelViewSet): 
    serializer_class = CommentSerializer 
 
    def get_queryset(self): 
        post = get_object_or_404(Post, pk=self.kwargs['post_id']) 
        return post.comments.all() 
 
    def perform_create(self, serializer): 
        serializer.save(author=self.request.user) 


class GroupViewSet(viewsets.ModelViewSet): 
    queryset = Group.objects.all() 
    serializer_class = GroupSerializer  


class FollowViewSet(viewsets.ModelViewSet): 
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)  
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'following__username'] 

    def get_queryset(self): 
        return Follow.objects.filter(following=self.request.user)

    def perform_create(self, serializer): 
        serializer.save(user=self.request.user) 
 