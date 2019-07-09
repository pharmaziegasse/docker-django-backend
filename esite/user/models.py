import json
import uuid
import django.contrib.auth.validators
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.core.fields import StreamField, RichTextField
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField, AbstractFormSubmission
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField, AbstractEmailForm, AbstractFormField, AbstractFormSubmission

# extend AbstractUser Model from django.contrib.auth.models
class User(AbstractUser):
    # AbstractUser.username field (modified max_length)
    username = models.CharField(null=True, blank=False, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 36 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=36, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')

    # AbstractUser Fields adjusted -> blank=False
    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)
    email = models.EmailField(_('email address'), blank=False)

    # new fields
    is_customer = models.BooleanField(blank=False, default=False)
    title = models.CharField(null=True, blank=False, max_length=12)
    birthdate = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=False)
    telephone = models.CharField(null=True, blank=False, max_length=40)
    address = models.CharField(null=True, blank=False, max_length=60)
    zipCode = models.CharField(null=True, blank=False, max_length=12)
    city = models.CharField(null=True, blank=False,max_length=60)
    country = models.CharField(null=True, blank=False,max_length=2)
    newsletter = models.BooleanField(null=True, blank=False)
    registration_data = models.TextField(null=True, blank=True)
    

    # new function to save user object
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = str(uuid.uuid4())

        super(User, self).save(*args, **kwargs)

    # Panels/fields to fill in the Add User form
    panels = [
        FieldPanel('is_customer'),
        FieldPanel('date_joined'),
        FieldPanel('title'),
        FieldPanel('first_name'),
        FieldPanel('last_name'),
        FieldPanel('email'),
        FieldPanel('telephone'),
        FieldPanel('address'),
        FieldPanel('zipCode'),
        FieldPanel('city'),
        FieldPanel('country'),
        FieldPanel('newsletter'),
        FieldPanel('registration_data'),
    ]

    def __str__(self):
        return str(self.username)