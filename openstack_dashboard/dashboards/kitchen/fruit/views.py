
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from horizon import forms

from openstack_dashboard.dashboards.kitchen.fruit \
    import forms as fruit_forms


class FruitView(forms.ModalFormView):
    form_class = fruit_forms.FruitForm
    form_id = "fruit_modal"
    modal_id = "fruit_modal"
    page_title = _("Fruit")
    submit_label = _("Show Message")
    submit_url = reverse_lazy("horizon:kitchen:fruit:index")
    template_name = 'kitchen/fruit/eat.html'
