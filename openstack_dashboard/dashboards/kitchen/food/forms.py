
import string

import babel
import babel.dates
from django.conf import settings
from django import shortcuts
from django.utils import encoding
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
import pytz

from horizon import forms
from horizon import messages
from horizon.utils import functions


class FoodForm(forms.SelfHandlingForm):
    name = forms.ChoiceField(label=_("Name"))
    teast = forms.ChoiceField(label=_("Teast"))

    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)

    def handle(self, request, data):
        response = shortcuts.redirect(request.build_absolute_uri())

        response = functions.save_config_value(
            request, response, 'FOOD_NAME', data['name'])
        
        response = functions.save_config_value(
            request, response, 'FOOD_TEAST', data['teast'])

        return response
