from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsStaffOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )



class IsAuthorOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return bool(
            #get access to superuser
            request.user.is_authenticated and
            request.user.is_superuser or
            #get access to author of object
            obj.author == request.user
        )


class IsSuperUserOrStaffReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            #get access to authors readonly
            request.method in SAFE_METHODS and
            request.user and
            request.user.is_staff or
            #get full access to superuser
            request.user and
            request.user.is_superuser
        )
