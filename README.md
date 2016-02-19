# README #

A bundle of several Python and Django utilities used by many department
applications.

As a convenience function use in requirements for django, bottle, uwsgi, redis and psycopg2 (postgresql) projects.

Future plans:

 * Include example uwsgi.ini file and supervisor configs for running
 * Include sample settings file for django to load a lot of stuff from env (uses django-confy)
 * Anything else repurposable across a lot of projects that changes a small amount (backend/util lib focused stuff, no ui components like templates/stylesheets and no data models)

## SSO Login Middleware ##

This will automatically login and create users using headers from an upstream proxy (REMOTE_USER and some others). The logout view will redirect to a separate logout page which clears the SSO session.

Install with pip, then add the following to django settings.py (note middleware must come after session and contrib.auth). Also note that the auth backend "django.contrib.auth.backends.ModelBackend" is in AUTHENTICATION_BACKENDS as this middleware depends on it for retrieving the logged in user for a session (will still work without it, but will reauthenticate the session on every request, and request.user.is_authenticated() won't work properly/will be false).

```
#!python
# settings.py
MIDDLEWARE_CLASSES = (
    ...,
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'dpaw_utils.middleware.SSOLoginMiddleware'
)
```

## Audit model mixin and middleware ##

``AuditMixin`` is an extension of ``Django.db.model.Model`` that adds a
number of additional fields:

 * creator - FK to ``AUTH_USER_MODEL``, used to record the object
   creator
 * modifier - FK to ``AUTH_USER_MODEL``, used to record who the object
   was last modified by
 * created - a timestamp that is set on initial object save
 * modified - an auto-updating timestamp (on each object save)

``AuditMiddleware`` is a middleware that will process any request for an
object having a ``creator` or ``modifier`` field, and automatically set those
to the request user via a ``pre_save`` signal.
