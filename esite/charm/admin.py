from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

# Register your charm related models here.

from esite.user.models import User

class CharmAdmin(ModelAdmin):
    pass

#modeladmin_register(CharmAdmin)
