from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to view or edit their own acc.
    """
    def has_object_permission(self, request, view, obj):
        # This must match the user making the request
        return obj.user == request.user