import json
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.core.fields import StreamField, RichTextField
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField, AbstractFormSubmission
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField, AbstractEmailForm, AbstractFormField, AbstractFormSubmission
from esite.user.models import User

class ProxyManager(BaseUserManager):
    def get_queryset(self):
        return super(ProxyManager, self).get_queryset().filter(is_customer=True)

class Customer(User):
    objects = ProxyManager()

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

    class Meta:
        proxy = True
        ordering = ('date_joined', )