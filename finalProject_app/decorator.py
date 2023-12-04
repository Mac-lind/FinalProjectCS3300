from django.http import HttpResponse
from django.shortcuts import redirect

#create a decorator for 
#pass in list of roles
def allowed_users(allowed_roles=[]):
    #create decorator and pass in view function
    #decorator is placed on top of view
    def decorator(view_func):
        #create wrapper function
        from django.http import HttpResponse
from functools import wraps  # Import wraps decorator for better preservation of function metadata

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper_func(request, *args, **kwargs):
            try:
                print('allowed_roles:', allowed_roles)
                group = None
                if request.user.groups.exists():
                    group = request.user.groups.all()[0].name
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse('You are not authorized to view this page')
            except Exception as e:
                # Log or print the exception for debugging
                print(f'Error in allowed_users decorator: {str(e)}')
                return HttpResponse('An error occurred while processing your request')
        return wrapper_func
    return decorator