from django.contrib.auth.views import login
from django.http import HttpResponseRedirect


def custom_login(request):
    """"""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return login(request)
