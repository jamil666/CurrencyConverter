from django import forms

class ChoiceSource(forms.Form):

        source_choice_field = forms.ChoiceField(choices=(
                ('AZN', 'AZN'),
                ('USD', 'USD'),
                ('EURO', 'EURO'),
                ('GBP', 'GBP')), required=False, label=False, )


class ChoiceDestination(forms.Form):
    destination_choice_field = forms.ChoiceField(choices=(
        ('AZN', 'AZN'),
        ('USD', 'USD'),
        ('EURO', 'EURO'),
        ('GBP', 'GBP')), required=False, label="", )


class Input(forms.Form):
    input_field = forms.FloatField(required=False, label=False)

