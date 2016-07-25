from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm

def login(request):
	c = {}
	c.update(csrf(request))
	request.session['username'] = 'PUBLIC'
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password= password)

	if user is not None:
		auth.login(request,user)
		request.session['username'] = username
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	return render_to_response('loggedin.html',
		{'full_name' : request.user.username, 'username' : request.session['username']})

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	request.session['username'] = 'PUBLIC'
	return render_to_response('logout.html')

def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success')


	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()
	print args
	return render_to_response('register.html',args)

def register_success(request):
	return render_to_response('register_success.html')