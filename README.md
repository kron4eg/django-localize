Purpose
=======

django-localize used to add language prefix to your URL without urls.py modifications.


Install
=======

Put localize somewhere in your sys.path (PYTHONPATH)

Add localize to settings.INSTALLED_APPS in !FIRST! position, for example

    INSTALLED_APPS = (
        'localize',
        'django.contrib.markup',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
    )

Add 'localize.middleware.LocaleURLMiddleware' to settings.MIDDLEWARE_CLASSES, for example

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'localize.middleware.LocaleURLMiddleware'
        'django.middleware.common.CommonMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.middleware.http.ConditionalGetMiddleware',
    )

It must be after !SessionMiddleware!


Define your languages in settings.LANGUAGES (you may combine it with gettext)

    LANGUAGES = (
        ('ru', 'Russian'),
        ('en', 'English'),
    )

Set settings.USE_I18N

    USE_I18N = True

Usage
=====

functions and template tag

    django.core.urlresolvers.reverse
    django.db.models.permalink
    {% url %} now works with

now accept locale parameter

Example
=======

models.py
---------

    from django.db import models
    from django.conf import settings

    class SomeModel(models.Model):
        lang = models.CharField(max_length=2, db_index=True, choices=settings.LANGUAGES)
        title = models.CharField(max_length=255)
        text = models.TextField()

        def __unicode__(self):
            return u'%s (%s)' % (self.title, self.lang)

        @models.permalink
        def get_absolute_url(self):
            return ('somemodel_namedurl_view', (), {
                'id': self.pk,
                'locale': self.lang,
            })

And now you able to do next:

    >>> from models import SomeModel
    >>> s = SomeModel.objects.get(pk=1)
    >>> s.get_absolute_url()
    /en/some_path/123/
