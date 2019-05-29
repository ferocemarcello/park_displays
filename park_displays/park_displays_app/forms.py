from django import forms


class CheckMultiCheckBox(forms.Form):
    '''(attrs={'class' : 'form-control'})'''
    gymselection = forms.MultipleChoiceField(label="Select Gym tools to show",widget=forms.CheckboxSelectMultiple,
                                               choices=[])
    def __init__(self,label=None, *args, **kwargs):
        super(CheckMultiCheckBox, self).__init__(*args, **kwargs)
        if label:
            self.fields['gymselection'].label=label