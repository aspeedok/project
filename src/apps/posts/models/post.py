from django.db import models


class Post(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="название",
    )
    text = models.TextField(verbose_name="текст")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="дата создания",
    )

    def __str__(self):
        return self.name
