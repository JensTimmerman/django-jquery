from django.conf import settings
from django.forms.utils import flatatt
from django.template import Library

from jquery.utils import jquery_path

register = Library()


@register.simple_tag
def jquery_script():
    return '<script{0}></script>'.format(flatatt({
        'type': 'text/javascript',
        'src': settings.MEDIA_URL + jquery_path,
    }))
