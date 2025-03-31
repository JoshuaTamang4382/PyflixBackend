from rest_framework.permissions import BasePermission

class IsAdminOrStaff(BasePermission):
    """
    Custom permission to allow only admin or staff users to perform write operations
    (POST, PUT, DELETE) on the movies API.
    All users (including guests) can read (GET) movie details or list.
    """

    def has_permission(self, request, view):
        # Allow read-only (GET) access to all users
        if request.method == "GET":
            return True
        
        # Allow write (POST, PUT, DELETE) only for admin or staff users
        user = request.user
        if user.is_authenticated and user.role in ['admin', 'staff']:
            return True
        return False

class IsPublic(BasePermission):
  
  pass
