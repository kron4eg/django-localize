# -*- coding: utf-8 -*-
from django.core import urlresolvers
from django.conf import settings
from django.utils import translation


def reverse(viewname, urlconf=None, args=[], kwargs={}, prefix=None):
    locale = kwargs.pop('locale', translation.get_language())
    path = django_reverse(viewname, urlconf, args, kwargs, prefix)
    script_prefix = urlresolvers.get_script_prefix()
    if settings.USE_I18N:
        path = script_prefix + locale + '/' + path.partition(script_prefix)[2]
    return path

django_reverse = urlresolvers.reverse
urlresolvers.reverse = reverse
