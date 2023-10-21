from rest_framework import  permissions

# Custom Permissions
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Authenticted users only can see the list view page
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request so we'll
        # always allow GET, HEAD, or OPTIONS request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the author of a post
        return obj.author == request.user
    
