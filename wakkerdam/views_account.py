
"""
	Een extra views bestand om overzicht te houden.
"""

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.views.decorators.http import require_POST


def login(request):
	if request.user.is_authenticated():
		""" This shows a simple text """
		return HttpResponse('You are already logged in, you may die!')
	""" AuthenticationForm is a standard Django login form (lazy) """
	form = AuthenticationForm(request = request, data = None)
	return render(request, 'login.html', {
		'form': form,
	})


def login_submit(request):
	if request.user.is_authenticated():
		""" This shows a simple text """
		return HttpResponse('You are already logged in!')
	form = AuthenticationForm(request = request, data = request.POST)
	if form.is_valid():
		""" Okay, login! """
		print 'valid!', form.get_user() # tijdelijk
		auth_login(request, form.get_user())
	else:
		print [unicode(m) for m in form.error_messages.values()] # tijdelijk
		""" Show the login form again - it will automatically show errors now """
		return render(request, 'login.html', {
			'form': form,
		})
	return redirect(to = reverse('wakkerdam_games_all'))


def register(request):
	if request.user.is_authenticated():
		""" This shows a simple text """
		return HttpResponse('You are already logged in!')
	""" UserCreationForm is a standard Django registration form """
	form = UserCreationForm(data = None)
	return render(request, 'register.html', {
		'form': form,
	})


def register_submit(request):
	if request.user.is_authenticated():
		""" This shows a simple text """
		return HttpResponse('You are already logged in!')
	form = UserCreationForm(data = request.POST)
	if form.is_valid():
		form.save()
		""" Let's also log in immediately """
		new_user = authenticate(username = request.POST['username'], password = request.POST['password1'])
		auth_login(request, new_user)
	else:
		return render(request, 'register.html', {
			'form': form,
		})
	return redirect(to = reverse('wakkerdam_games_all'))


@login_required
def logout(request):
	"""
		In this case the form is 'empty': only a button (and a csrf token), so we will just use html, no special Django
		form object magic.
	"""
	return render(request, 'logout.html')


@require_POST
def logout_submit(request):
	"""
		You would think that no form is needed for logout, because there is no data. You could create a simple link.
		That would work but it would be insecure. Not very, but under some conditions you can log out other people.
		Django requires CSRF tokens for every POST request, so @require_POST also means CSRF-safe.
	"""
	auth_logout(request)
	return redirect(to = reverse('wakkerdam_games_all'))


