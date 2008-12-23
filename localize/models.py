# -*- coding: utf-8 -*-
from django.core import urlresolvers
from django.conf import settings
from django.utils import translation


def reverse(viewname, urlconf=None, args=[], kwargs={}):
    locale = kwargs.pop('locale', translation.get_language())
    path = django_reverse(viewname, urlconf, args, kwargs)
    if settings.USE_I18N:
        path = u'/' + locale + path
    return path

django_reverse = urlresolvers.reverse
urlresolvers.reverse = reverse
