from django import forms

class CheckMultiCheckBox(forms.Form):
    '''(attrs={'class' : 'form-control'})'''
    gymselection = forms.MultipleChoiceField(label="Select Gym tools to show",widget=forms.CheckboxSelectMultiple,
                                               choices=[])
    def __init__(self,gymchoices=None, *args, **kwargs):
        super(CheckMultiCheckBox, self).__init__(*args, **kwargs)
        if gymchoices:
            self.fields['gymchoices'].widget.attrs['size'] = '30'
            self.fields['gymchoices'].choices = gymchoices
            self.fields['gymchoices'].initial=[x[0] for x in self.fields['gymchoices'].choices]