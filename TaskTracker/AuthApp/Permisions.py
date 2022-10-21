from django.core.handlers.wsgi import WSGIRequest
from rest_framework.permissions import BasePermission

from AuthApp.models import Moderator


class IsModerator(BasePermission):
    """разграничение доступа для админки"""
    def has_permission(self, request: WSGIRequest, view):
        if (request.user.is_authenticated and Moderator.objects.filter(
                user=request.user).exists()) or request.user.is_superuser:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        return True
