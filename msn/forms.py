from django.forms import ModelForm
from msn.models import Bericht

class BerichtForm(ModelForm):
    class Meta:
        model=Bericht
        fields = ['user', 'msg']


