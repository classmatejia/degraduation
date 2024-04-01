from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class McisLoggedIn(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        se = request.session.get('merchant', None)
        if se is None:
            return redirect('login')
        else:
            pass
