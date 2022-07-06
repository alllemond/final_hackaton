from rest_framework.permissions import BasePermission


class IsRatingAuthor(BasePermission):
    def has_object_permissions(self, request, view, obj):
        return request.user.is_authenticated and request.user == obj.author
       