from django import forms

class CheckMultiCheckBox(forms.Form):
    '''(attrs={'class' : 'form-control'})'''
    selection = forms.MultipleChoiceField(label="",widget=forms.CheckboxSelectMultiple, choices=[])

    def __init__(self,label=None,choices=[],*args, **kwargs):
        super(CheckMultiCheckBox, self).__init__(*args, **kwargs)
        if label and len(choices)>0:
            self.fields['selection'].widget.attrs['size'] = '30'
            self.fields['selection'].label=label
            self.fields['selection'].choices = choices
            self.fields['selection'].initial = [x[0] for x in self.fields['selection'].choices]

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