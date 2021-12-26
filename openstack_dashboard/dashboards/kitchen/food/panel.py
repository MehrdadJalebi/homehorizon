
from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.kitchen import dashboard


class FoodPanel(horizon.Panel):
    name = _("Food Panel")
    slug = 'food'


dashboard.Kitchen.register(FoodPanel)
