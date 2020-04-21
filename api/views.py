#api/views.py
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import F
from blog.models import Post, Comment
from . import serializers

@api_view(['GET'])
def index(request):
    return Response()

class PostListView(generics.ListAPIView):
    """
    Returns a list of published posts
    """
    serializer_class = serializers.PostListSerializer
    queryset = Post.objects.published()

class PostDetailView(generics.RetrieveAPIView):
    """
    Returns post details
    """
    serializer_class = serializers.PostDetailSerializer
    queryset = Post.objects.published()

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        post_id = self.request.query_params.get('post')
        queryset = super().get_queryset()
        if post_id and post_id.isdecimal():
            queryset = queryset.filter(post_id=int(post_id))

        return queryset.order_by('-created')

class CommentView(generics.RetrieveAPIView):
    serializer_class = serializers.CommentSerializer
    queryset = Comment.objects.all()

class CommentlikeView(generics.RetrieveAPIView):
    def get_object(self, pk):
        return Comment.objects.get(pk=pk)


    def get(self, request, pk):
        full_request_url = request.build_absolute_uri()
        if 'dislike' in full_request_url:
            comment = self.get_object(pk=pk)
            comment.dislikes += 1
            comment.save()
            serializer = serializers.CommentSerializer(comment)
            return Response(serializer.data)
        elif 'like' in full_request_url:
            comment = self.get_object(pk=pk)
            comment.likes += 1
            comment.save()
            serializer = serializers.CommentSerializer(comment)
            return Response(serializer.data)
