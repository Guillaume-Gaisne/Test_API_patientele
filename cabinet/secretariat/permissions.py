from rest_framework.permissions import BasePermission

class IsAdminAuthenticated(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET' and view.action in ['list', 'retrieve']:
            return True
        else:
            return bool(request.user
                and request.user.is_authenticated
                and request.user.is_superuser
            )
