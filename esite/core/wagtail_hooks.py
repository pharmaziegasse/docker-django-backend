from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html

from wagtail.core import hooks

@hooks.register("insert_global_admin_css", order=100)
def global_admin_css():
    # load CSS file custom.css in static/core/
    return format_html('<link rel="stylesheet" href="{}">', static("core/custom.css"))