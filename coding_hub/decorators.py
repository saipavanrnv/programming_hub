from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            superusers = User.objects.filter(is_superuser=True)
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles or superusers:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator
