from django.shortcuts import render
from irc.models import Memo
from irc.forms import MemoForm

def irc(request):
    allmemos = Memo.objects.all
    form=MemoForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'irc.html', {
        'allmemos':allmemos,
        'form': form,
    })
# Create your views here.
