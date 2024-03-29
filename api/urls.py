from django.urls import path, include
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )
from rest_framework.routers import DefaultRouter 
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router = DefaultRouter() 
 
router.register('posts', PostViewSet, basename='posts') 
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments') 
router.register('group', GroupViewSet, basename='group') 
router.register('follow', FollowViewSet, basename='follow') 


urlpatterns = [
        path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('', include(router.urls)), 
    ] 
    