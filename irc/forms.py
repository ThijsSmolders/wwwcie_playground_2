from django.forms import ModelForm
from irc.models import Memo

class MemoForm(ModelForm):
    class Meta:
        model=Memo