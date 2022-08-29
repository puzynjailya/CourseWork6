from django.contrib.auth import get_user_model
from django.db import models

from ads.models import Advertisement

User = get_user_model()


class Comment(models.Model):
    text = models.CharField(max_length=3000, blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    ad = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ("id",)


