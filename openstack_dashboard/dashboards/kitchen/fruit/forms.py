
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
    current_password = forms.CharField(
        label=_("Current password"),
        widget=forms.PasswordInput(render_value=False))
    new_password = forms.RegexField(
        label=_("New password"),
        widget=forms.PasswordInput(render_value=False),
        regex=validators.password_validator(),
        error_messages={'invalid':
                        validators.password_validator_msg()})
    confirm_password = forms.CharField(
        label=_("Confirm new password"),
        widget=forms.PasswordInput(render_value=False))
    no_autocomplete = True

    def clean(self):
        '''Check to make sure password fields match.'''
        data = super(PasswordForm, self).clean()
        if 'new_password' in data:
            if data['new_password'] != data.get('confirm_password', None):
                raise ValidationError(_('Passwords do not match.'))
            if data.get('confirm_password', None) == \
                    data.get('current_password', None):
                raise ValidationError(_('Old password and new password '
                                        'must be different'))
        return data

    # We have to protect the entire "data" dict because it contains the
    # oldpassword and newpassword strings.
    @sensitive_variables('data')
    def handle(self, request, data):
        user_is_editable = api.keystone.keystone_can_edit_user()

        if user_is_editable:
            try:
                api.keystone.user_update_own_password(request,
                                                      data['current_password'],
                                                      data['new_password'])
                response = http.HttpResponseRedirect(settings.LOGOUT_URL)
                msg = _("Password changed. Please log in again to continue.")
                utils.add_logout_reason(request, response, msg)
                return response
            except Exception:
                exceptions.handle(request,
                                  _('Unable to change password.'))
                return False
        else:
            messages.error(request, _('Changing password is not supported.'))
            return False
