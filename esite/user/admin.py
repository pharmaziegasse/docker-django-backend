from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)

from .models import User

class UserAdmin(ModelAdmin):
    model = User
    menu_label = "User"
    menu_icon = "user"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
   
    # Listed in the user overview
    list_display = ('date_joined', 'username', 'title', 'first_name', 'last_name', 'email', 'telephone', 'address', 'zipCode', 'city', 'country', 'newsletter')
    search_fields = ('date_joined', 'title', 'first_name', 'last_name', 'email', 'telephone', 'address', 'zipCode', 'city', 'country', 'newsletter')

#modeladmin_register(UserAdmin)
