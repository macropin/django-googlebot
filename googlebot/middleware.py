import socket

from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User


class GooglebotMiddleware(object):
    """
    Middleware to automatically log in the Googlebot with the user account 'googlebot'
    """
    def process_request(self, request):
        request.is_googlebot = False # Assume false, until proven
        if request.user == AnonymousUser():
            if 'Googlebot' in request.META['HTTP_USER_AGENT']:
                try:
                    remote_ip = request.META['REMOTE_ADDR']
                    hostname = socket.gethostbyaddr(remote_ip)[0]

                    if hostname.endswith('googlebot.com'):
                        request.user = User.objects.get_or_create(username='googlebot') # login our googlebot user :)
                        request.is_googlebot = True
                    else:
                        # FAKE googlebot!!!!
                        request.is_googlebot = False

                except Exception, e:
                    pass # Don't bring down the site
        return None
