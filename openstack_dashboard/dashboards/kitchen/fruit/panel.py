
from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.kitchen import dashboard


class FruitPanel(horizon.Panel):
    name = _("Fruit Panel")
    slug = 'fruit'


dashboard.Kitchen.register(FruitPanel)
