from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UserProfileListAPIView,UserProfileDetailAPIView, PostDetailAPIView,PostListAPIView, PostLikeViewSet,
                    PostContentViewSet, FollowViewSet, FavoriteViewSet,
                    FavoriteItemViewSet, HashtagViewSet, CommentViewSet,
                    CommentLikeViewSet,RegisterView,LoginView,LogoutView)

router = DefaultRouter()
router.register(r'post-likes', PostLikeViewSet)
router.register(r'post-contents', PostContentViewSet)
router.register(r'follows', FollowViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'favorite-items', FavoriteItemViewSet)
router.register(r'hashtags', HashtagViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'comment-likes', CommentLikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('post/',PostListAPIView.as_view(),name='post_list'),
    path('post/<int:pk>',PostDetailAPIView.as_view(),name='post_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]