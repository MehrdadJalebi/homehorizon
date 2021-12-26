
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from horizon import forms
from horizon.utils import functions as utils
from openstack_dashboard.dashboards.kitchen.food import forms as food_forms


class FoodView(forms.ModalFormView):
    form_class = food_forms.FoodForm
    form_id = "food_modal"
    modal_id = "food_modal"
    page_title = _("Food")
    submit_label = _("Save")
    submit_url = reverse_lazy("horizon:kitchen:food:index")
    template_name = 'kitchen/food/cook.html'

    def get_initial(self):
        return {
            'name': 'pizza',
            'teast': 'best',

    def form_valid(self, form):
        return form.handle(self.request, form.cleaned_data)
