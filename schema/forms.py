from django import forms

from schema.models import Schema, Column

ColumnFormSet = forms.inlineformset_factory(
    Schema, Column, fields=('name', 'type', 'range_from', 'range_to', 'order'), extra=4
)


class CSVForm(forms.ModelForm):
    columns = ColumnFormSet()

    class Meta:
        model = Schema
        exclude = ('user',)
