from django.core.exceptions import PermissionDenied


def is_admin(view):
    def wrap(request, *args, **kwargs):
        if request.user.is_superuser:
            return view(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap
