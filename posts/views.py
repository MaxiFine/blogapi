from rest_framework import generics

from .models import Post
from .permissions import IsAuthorOrReadOnly  # Custom Permissions
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  # view level Permissions
    queryset = Post.objects.all()
    serializer_class = PostSerializer

