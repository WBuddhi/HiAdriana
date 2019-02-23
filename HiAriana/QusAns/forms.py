from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class QA_Form(forms.Form):
    Choice = forms.ChoiceField(label = '', widget = forms.RadioSelect)
