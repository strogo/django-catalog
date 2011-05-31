from django.conf import settings
import os.path
import sys

# TODO: migrate to django.db.models.loader rather than import modules manually
DEFAULT_CATALOG_MODELS = [
    ('defaults', 'Item'),
    ('defaults', 'Section'),
]

CATALOG_MODELS = getattr(settings, 'CATALOG_MODELS', DEFAULT_CATALOG_MODELS)

DEFAULT_MPTT = 'mptt' in settings.INSTALLED_APPS
CATALOG_MPTT = getattr(settings, 'CATALOG_MPTT', DEFAULT_MPTT)

# TODO: Extend existing SERIALIZATION_MODULES
settings.SERIALIZATION_MODULES = {
    'catalog_extdirect' : 'catalog.grid_to_json',
}

# CATALOG_FILTERS
#Acceptable values:
#For all models:
#    
#    CATALOG_FILTER = Q(show=True)
#
#Or per-model:
#    
#    CATALOG_FILTER = {
#        'defauls.Section': Q(show=True),
#        'defauls.Item': Q(hidden=False), 
#    }