from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

User = get_user_model()


class Advertisement(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    price = models.PositiveIntegerField(blank=False, null=False, validators=[MinValueValidator(1)])
    description = models.TextField(max_length=1500, blank=True, null=False, default='Input your text here')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='ads_images/', blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ('-created_at',)
