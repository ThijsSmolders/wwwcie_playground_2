from django.shortcuts import render
from msn.models import Bericht
from msn.forms import BerichtForm

def msn_chat(request):
    all_msg = Bericht.objects.all()
    form=BerichtForm(request.POST)
    return render(request, 'msn_test.html', {'all_msg':all_msg})
