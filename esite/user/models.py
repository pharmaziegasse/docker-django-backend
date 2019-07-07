import json
import uuid
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

class User(AbstractUser):
    # AbstractUser.username used as uuid field
    username = models.CharField(null=True, blank=False, unique=True, verbose_name="uuid", default=str(uuid.uuid4()), max_length=36)
    
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
        return self.username