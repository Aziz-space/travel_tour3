from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied("Доступ только для администраторов")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
