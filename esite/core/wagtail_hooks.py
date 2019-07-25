from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html
from django.http import HttpResponse

from wagtail.core import hooks

@hooks.register("insert_global_admin_css", order=100)
def global_admin_css():
    # Add /static/css/custom.css to admin.
    return format_html('<link rel="stylesheet" href="{}">', static("core/custom.css"))

@hooks.register('before_serve_document')
def serve_pdf(document, request):
    if document.file_extension != 'pdf':
        return  # Empty return results in the existing response
    response = HttpResponse(document.file.read(), content_type='application/pdf')
    response['Content-Disposition'] = 'filename="' + document.file.name.split('/')[-1] + '"'
    if request.GET.get('download', False) in [True, 'True', 'true']:
        response['Content-Disposition'] = 'attachment; ' + response['Content-Disposition']
    return response
