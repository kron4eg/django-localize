# -*- coding: utf-8 -*-
import re
from django.conf import settings
from django.core.urlresolvers import get_script_prefix
from django.http import HttpResponsePermanentRedirect
from django.middleware.locale import LocaleMiddleware
from django.utils import translation


class LocaleURLMiddleware(LocaleMiddleware):
    """
    This middleware forces LANGUAGE_CODE prefix for your urls (exclude NON_I18N_URLS).
    It can be easily disabled or enabled using USE_I18N setting.
    """
    def __init__(self):
        self.supported = dict(settings.LANGUAGES)
        self.url_check_re = re.compile(r'^/(?P<locale>%s)(?P<path>.*)$' % \
            ('|'.join(self.supported.keys())))

    def remember_lang(self, request, lang):
        if hasattr(request, 'session'):
            request.session['django_language'] = lang

    def process_request(self, request):
        language = translation.get_language_from_request(request)[:2]
        request.LANGUAGE_CODE = language
        script_prefix = get_script_prefix()
        if not settings.USE_I18N:
            return None

        check = self.url_check_re.match(request.path_info)
        if check:
            url_lang, url_path = check.groupdict().values()
            if not url_path:
                return HttpResponsePermanentRedirect('%s%s/' % (script_prefix, url_lang))
            url_list = url_path.split('/')
            request.path = request.path_info = request.META['PATH_INFO'] \
                    = u'/'.join(url_list)
            self.remember_lang(request, url_lang)
            translation.activate(url_lang)
            request.LANGUAGE_CODE = url_lang
            return None

        if 'POST' in request.method:
            translation.activate(language)
            return None

        redirect_url = u'%s%s%s' % (script_prefix, language, request.path_info)
        for url in getattr(settings, 'NON_I18N_URLS', ()):
            if request.path_info.startswith(url):
                return None
        return HttpResponsePermanentRedirect(redirect_url)

    def process_response(self, request, response):
        resp = super(LocaleURLMiddleware, self).process_response(request, response)
        if settings.USE_I18N:
            resp.set_cookie('django_language', request.LANGUAGE_CODE, 60*60*24*365)
        return resp
