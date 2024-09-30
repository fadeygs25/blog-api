from rest_framework import viewsets
from .serializers import BlogPostSerializer
from .services.blog_service import BlogPostService

class BlogPostViewSet(viewsets.ViewSet):
    def list(self, request):
        posts = BlogPostService.list_all_posts()
        serializer = BlogPostSerializer(posts, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        post = BlogPostService.retrieve_post(pk)
        serializer = BlogPostSerializer(post)
        return Response(serializer.data)

    def create(self, request):
        post = BlogPostService.create_new_post(request.data)
        serializer = BlogPostSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk=None):
        post = BlogPostService.update_existing_post(pk, request.data)
        serializer = BlogPostSerializer(post)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        BlogPostService.delete_existing_post(pk)
        return Response(status=204)
