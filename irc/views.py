from django.shortcuts import render
from irc.models import Memo

def irc(request):
    allmemos = Memo.objects.all
    return render(request,'irc.html',{'allmemos':allmemos})

# Create your views here.
