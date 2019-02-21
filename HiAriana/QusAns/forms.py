from django import forms
from uploads.core.models import QusJsonFile

class DocumentForm(forms.ModelForm):
    class Meta:
        model = QusJsonFile
        fields = {'document',}
