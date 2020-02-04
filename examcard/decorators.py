from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.conf import settings

def superuser_only(function):
    """Limit view to superusers only."""

    def _inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied    
        return function(request, *args, **kwargs)
    
    return _inner


# The way to use this decorator is:
# @superuser_only

def anonymous_required(function=None, redirect_url=None):
    if not redirect_url:
        redirect_url = settings.LOGIN_REDIRECT_URL
        
    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous(),
        login_url=redirect_url
    )
    if function:
        return actual_decorator(function)
    
    return actual_decorator

# @anonymous_required