# Django middleware to allow googlebot to index logged-in accessible content

Django Middleware to allow Googlebot access to paywalled, or login only content. 
This Django middleware automatically logs in Googlebot as the _googlebot_ user.

## Install

Add to your system / virtualenv:

    pip install git+git://github.com/cyeong/django-googlebot#egg=django-googlebot

Add to Django _settings.py_:

    MIDDLEWARE_CLASSES = (
        ...
        'googlebot.middleware.GooglebotMiddleware',
    )

Finally, create a _googlebot_ user. This account will be used when Googlebot is automatically logged in.
If you don't create an account, then one will be created automatically.

NB If you wish to disable the Google Cache feature, create a _robots.txt_ with _Noarchive_ . Eg:

    User-agent: *
    Disallow:
    Noarchive: /restricted-content/
