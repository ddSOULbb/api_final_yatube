from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet, 'posts')
router.register('groups', views.GroupViewSet, 'groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet, 'comments')
router.register('follow', views.FollowViewSet, 'follow')

urlpatterns = [
    path('v1/', include(router.urls)),
]
