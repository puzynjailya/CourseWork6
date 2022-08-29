from django.shortcuts import render
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.models import Advertisement
from reviews.models import Comment
from reviews.serializers import CommentViewSerializer
from users.permissions import IsOwner, IsAdmin


@extend_schema_view(
    list=extend_schema(
        description='Получение списка комментариев',
        summary='Список комментариев'
    ),
    retrieve=extend_schema(
        description='Получение одного комментария по ID',
        summary='Один комментарий'
    ),
    create=extend_schema(
        description='Создание комментария по ID',
        summary='Создание комментария'
    ),
    destroy=extend_schema(
        description='Удаление комментария по ID',
        summary='Удаление комментария'
    ),
    update=extend_schema(
        description='Обновление комментария по ID',
        summary='Обновление комментария'
    ),
)
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentViewSerializer
    permission_classes = [AllowAny,]

    def perform_create(self, serializer):
        ad_id = self.kwargs.get("ad_pk")
        ad_instance = get_object_or_404(Advertisement, id=ad_id)
        user = self.request.user
        serializer.save(author=user, ad=ad_instance)

    def get_queryset(self):
        ad_id = self.kwargs.get("ad_pk")
        ad_instance = get_object_or_404(Advertisement, id=ad_id)
        return ad_instance.comments.all()

    def get_permissions(self):
        permission_classes = [IsAuthenticated, ]
        if self.action in ['retrieve', 'list']:
            permission_classes = [IsAuthenticated,]
        else:
            permission_classes = [IsOwner | IsAdmin]
        return tuple(permission() for permission in permission_classes)