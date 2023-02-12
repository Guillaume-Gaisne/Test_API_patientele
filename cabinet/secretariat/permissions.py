from rest_framework.permissions import BasePermission

class IsAdminAuthenticated(BasePermission):

    def has_permission(self, request, view):
        # Putting permissions only on the 'GET' request, preventing anyone
        # to modify the informations in the database
        if request.method == 'GET':
            return True
        else:
            return bool(request.user
                and request.user.is_authenticated
                and request.user.is_superuser
            )
