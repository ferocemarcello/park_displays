from django import forms
from django.forms.widgets import NumberInput

class CheckMultiCheckBox(forms.Form):
    '''(attrs={'class' : 'form-control'})'''
    selection = forms.MultipleChoiceField(label="",widget=forms.CheckboxSelectMultiple, choices=[])

    def __init__(self,label=None, *args, **kwargs):
        super(CheckMultiCheckBox, self).__init__(*args, **kwargs)
        if label:
            self.fields['selection'].label=label

class CheckBox(forms.Form):
    selection = forms.ChoiceField(label="", widget=forms.RadioSelect, choices=[])

    def __init__(self,label=None, *args, **kwargs):
        super(CheckBox, self).__init__(*args, **kwargs)
        if label:
            self.fields['selection'].label=label

class Dropdown(forms.Form):
    selection = forms.ChoiceField(label="", widget=forms.Select, choices=[])

    def __init__(self,label=None, *args, **kwargs):
        super(Dropdown, self).__init__(*args, **kwargs)
        if label:
            self.fields['selection'].label=label