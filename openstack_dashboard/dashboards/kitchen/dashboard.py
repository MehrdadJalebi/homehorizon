from django.utils.translation import ugettext_lazy as _

import horizon


class Kitchen(horizon.Dashboard):
    name = _("Kitchen")
    slug = "kitchen"
    panels = ('food', 'fruit')
    default_panel = 'food'

horizon.register(Kitchen)
