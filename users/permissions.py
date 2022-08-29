from django.contrib.auth import get_user_model
from rest_framework import permissions

from users.models import UserRoles

User = get_user_model()


class IsOwner(permissions.BasePermission):
    message = 'Это мой мессадж! Тут может хулиганить только владелец подборки!'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.author_id:
            return True
        return False


class IsAdmin(permissions.BasePermission):
    message = 'Здесь хулиганить могут только Админы, т.е. те, кому все дозволенно!'

    def has_permission(self, request, view):
        if request.user.role == UserRoles.ADMIN:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.role == UserRoles.ADMIN:
            return True
        return False
