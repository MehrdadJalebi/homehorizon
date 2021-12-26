
from django.conf import settings
from django.forms import ValidationError
from django import http
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.debug import sensitive_variables

from horizon import exceptions
from horizon import forms
from horizon import messages
from horizon.utils import functions as utils
from horizon.utils import validators

from openstack_dashboard import api


class FruitForm(forms.SelfHandlingForm):
    name = forms.CharField(label=_("Name"))
    color = forms.CharField(label=_("Color"))
    no_autocomplete = True

    def handle(self, request, data):
        messages.error(request, _('Hi! Fruits is Good'))
        return True
