from django.conf import settings
import os.path
import sys

DEFAULT_CATALOG_CONNECTED_MODELS = [
    ('catalog.defaults.models.Item', 'catalog.defaults.admin.ItemAdmin'),
    ('catalog.defaults.models.Section', 'catalog.defaults.admin.SectionAdmin'),
]

DEFAULT_TINYMCE = 'tinymce' in settings.INSTALLED_APPS
CATALOG_TINYMCE = getattr(settings, 'CATALOG_TINYMCE', DEFAULT_TINYMCE)

DEFAULT_MPTT = 'mptt' in settings.INSTALLED_APPS
CATALOG_MPTT = getattr(settings, 'CATALOG_MPTT', DEFAULT_MPTT)

DEFAULT_IMAGEKIT = 'imagekit' in settings.INSTALLED_APPS
CATALOG_IMAGEKIT = getattr(settings, 'CATALOG_IMAGEKIT', DEFAULT_IMAGEKIT)

# how urls will look like
# you may set 'id', 'slug' or 'combo' values
CATALOG_URL_SCHEME = getattr(settings, 'CATALOG_URL_SCHEME', 'id')
CATALOG_ROOT_PAGE = getattr(settings, 'CATALOG_ROOT_PAGE', True)
