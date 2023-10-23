# from django.urls import path
# from .views import PostList, PostDetail, UserDetail,UserList


# urlpatterns = [
#     path('', PostList.as_view(), name='list_posts'),
#     path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
#     path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
#     path('users/', UserList.as_view(), name='users'),
     

# ]

# USING ROUTERS FOR URLS


from rest_framework.routers import SimpleRouter

from .views import PostViewSet, UserViewSet


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls

