from django import forms
from QusAns.models import QusJsonFile

class DocumentForm(forms.ModelForm):
    class Meta:
        model = QusJsonFile
        fields = {'document',}
