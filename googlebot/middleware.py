import socket

from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User


class GooglebotMiddleware(object):

    def process_request(self, request):
        if request.user == AnonymousUser():
            request.is_googlebot = False # Assume false, until proven
            if 'Googlebot' in request.META['HTTP_USER_AGENT']:
                try:
                    remote_ip = request.META['REMOTE_ADDR']
                    hostname, aliaslist, ipaddrlist = str(socket.gethostbyaddr(remote_ip))

                    if hostname.endswith('googlebot.com.'):
                        request.user = User.objects.get(username='googlebot') # login our googlebot user :)
                        request.is_googlebot = True
                    else:
                        # FAKE googlebot!!!!
                        request.is_googlebot = False

                except Exception, e:
                    pass # Don't bring down the site
        return None
