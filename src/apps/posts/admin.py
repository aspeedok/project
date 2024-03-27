from django.contrib import admin
from apps.posts.models.post import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("name", "text", "created_at")
    search_fields = ("name", "text")
    list_filter = ("created_at",)
