from django.utils.translation import gettext as _
from django.db.models import CharField

DAYS = {
    '1': _(u'Monday'),
    '2': _(u'Tuesday'),
    '3': _(u'Wednesday'),
    '4': _(u'Thursday'),
    '5': _(u'Friday'),
    '6': _(u'Saturday'),
    '7': _(u'Sunday')
}


class DaysField(CharField):
    def __init__(self, *args, **kwargs):
        kwargs["choices"] = tuple(sorted(DAYS.items()))
        kwargs["max_length"] = 1
        super(DaysField, self).__init__(*args, **kwargs)
