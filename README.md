# Django Middleware to allow GoogleBot to access and index restricted content


NB Remeber to create a _robots.txt_ with _Noarchive_ if you wish to disable the Google Cache feature.

    User-agent: *
    Disallow:
    Noarchive: /download/
