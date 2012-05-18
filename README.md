# Allow Googlebot to access and index restricted content

Django Middleware to allow Googlebot access to paywalled, or login only content. 
This Django middleware automatically logs in Googlebot as the _googlebot_ user.

## Install

Add to your system / virtualenv:

    pip install -e git+git://github.com/macropin/django-googlebot#egg=django-googlebot

Add to Django _settings.py_:

    MIDDLEWARE_CLASSES = (
        ...
        'googlebot.middleware.GooglebotMiddleware',
    )


NB Remeber to create a _robots.txt_ with _Noarchive_ if you wish to disable the Google Cache feature. Eg:

    User-agent: *
    Disallow:
    Noarchive: /download/
