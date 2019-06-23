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

    def __init__(self,label=None, choices=[], *args, **kwargs):
        super(Dropdown, self).__init__(*args, **kwargs)
        if label and len(choices)>0:
            self.fields['selection'].label=label
            self.fields['selection'].choices = choices

class Slider(forms.Form):
    intensity = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step':'1', 'min':'0', 'max':'100'}), label="")

    def __init__(self,label=None, *args, **kwargs):
        super(Slider, self).__init__(*args, **kwargs)
        self.fields['intensity'].widget.attrs.update({'type': 'range'})
        self.fields['intensity'].widget.attrs.update({'step': '1'})
        self.fields['intensity'].widget.attrs.update({'min': '0'})
        self.fields['intensity'].widget.attrs.update({'max': '100'})
        self.fields['intensity'].label=label