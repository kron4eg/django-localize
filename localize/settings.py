from django.conf import settings

NON_I18N_URLS = getattr(settings, 'NON_I18N_URLS', (settings.MEDIA_URL, settings.ADMIN_MEDIA_PREFIX))

