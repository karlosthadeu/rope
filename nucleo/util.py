from django.utils import timezone
import os
from uuid import uuid4


def renomear_foto(instance, filename):
    upload_to = 'avatares_usuarios'
    ext = filename.split('.')[-1]

    if instance.pk:
        filename = '{}{}.{}'.format(instance.pk, uuid4().hex, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)

"""
    Disponível em:
        dangtrinh.com/2015/11/django-imagefield-rename-file-on-upload.html
"""




