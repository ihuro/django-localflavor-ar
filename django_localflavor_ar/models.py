from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import CharField
from django_localflavor_ar.ar_provinces import PROVINCE_CHOICES


class ARProvinceField(CharField):
    """
    A model field that stores the one-letter Argentinian province abbreviation
    in the database.
    """

    description = _("Argentina province (one uppercase letter)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = PROVINCE_CHOICES
        kwargs['max_length'] = 1
        super(ARProvinceField, self).__init__(*args, **kwargs)


class ARPostalCodeField(CharField):
    """
    A model field that forms represent as a forms.ARPostalCodeField field and
    stores the four-digit Argentinian postal code or an eight-digit CPA.
    """
    description = _("Argentinian postal code or CPA")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 8
        super(ARPostalCodeField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from forms import ARPostalCodeField as ARPostalCodeFormField
        defaults = {'form_class': ARPostalCodeFormField}
        defaults.update(kwargs)
        return super(ARPostalCodeField, self).formfield(**defaults)


class ARDNIField(CharField):
    """
    A model field that forms represent as a forms.ARDNIField field and
    stores the eight-digit Argentinian DNI.
    """
    description = _("Argentinian DNI")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 8
        super(ARDNIField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from forms import ARDNIField as ARDNIFormField
        defaults = {'form_class': ARDNIFormField}
        defaults.update(kwargs)
        return super(ARDNIField, self).formfield(**defaults)


class ARCUITField(CharField):
    """
    A model field that forms represent as a forms.ARCUITField field and
    stores the Argentinian CUIT/CUIL.
    """
    description = _("Argentinian CUIT/CUIL")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 13
        super(ARCUITField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from forms import ARCUITField as ARCUITFormField
        defaults = {'form_class': ARCUITFormField}
        defaults.update(kwargs)
        return super(ARCUITField, self).formfield(**defaults)
