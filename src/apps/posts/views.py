from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.posts.models.post import Post
from apps.posts.serializers import PostSerializer


@method_decorator(csrf_exempt, name="dispatch")
class PostCreateView(CreateView):
    model = Post
    template_name = "index.html"
    fields = ["name", "text"]
    success_url = reverse_lazy("create-post")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post created successfully!")
        return super().form_valid(form)


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
