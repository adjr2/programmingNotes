from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UpdateThreshold(forms.Form):
    threshold = forms.FloatField(
        help_text="Enter the threshold for the benchmark.",
        widget=forms.NumberInput(attrs={"id": "threshold_id"}),
    )

    def clean_renewal_date(self):
        data = self.cleaned_data["threshold"]

        # Check if a threshold is positive value.
        if data < 0:
            raise ValidationError(_("Invalid threshold - cannot be a negative value."))

        # Remember to always return the cleaned data.
        return data
