import json
import uuid
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from modelcluster.fields import ParentalKey
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


# Model manager to use in Proxy model
class ProxyManager(BaseUserManager):
    def get_queryset(self):
        # filter the objects for non-customer datasets based on the User model
        return super(ProxyManager, self).get_queryset().filter(is_active=False)

class Registration(User):
    # call the model manager on user objects
    objects = ProxyManager()

    # Panels/fields to fill in the Add Registration form
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


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')

class FormPage(AbstractEmailForm):
    # When creating a new Form page in Wagtail
    registration_head = models.CharField(null=True, blank=False, max_length=255)

    content_panels = [
        FieldPanel('registration_head', classname="full title"),
    ]

    def get_submission_class(self):
        return RegistrationFormSubmission

    # Create a new user
    def create_user(self, title, first_name, last_name, email, telephone, address, city, country, newsletter, registration_data):
        user = get_user_model()(
            username=uuid.uuid4(),
            is_customer=False,
            title=title,
            first_name=first_name,
            last_name=last_name,
            email=email,
            telephone=telephone,
            address=address,
            #zip_code=zip_code,
            city=city,
            country=country,
            newsletter=False,
            #verified=True,
            registration_data=registration_data,
        )

        user.set_password("password")
        user.save()

        return user

    # Called when a user registers
    def process_form_submission(self, form):
        user=self.create_user(
            title=form.cleaned_data['title'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            email=form.cleaned_data['email'],
            telephone=form.cleaned_data['telephone'],
            address=form.cleaned_data['address'],
            #zip_code=form.cleaned_data['zip_code'],
            city=form.cleaned_data['city'],
            country=form.cleaned_data['country'],
            newsletter=form.cleaned_data['newsletter'],
            #verified=form.cleaned_data['verified'],
            registration_data=json.dumps(form.cleaned_data, cls=DjangoJSONEncoder),
        )

        self.get_submission_class().objects.create(
            form_data=json.dumps(form.cleaned_data, cls=DjangoJSONEncoder),
            page=self,
            user=user,
        )

class RegistrationFormSubmission(AbstractFormSubmission):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
