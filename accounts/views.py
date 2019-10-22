from django.shortcuts import render, redirect
from django.contrib import auth
from django.template.context_processors import csrf


def login(request):
	args = {}
	args.update(csrf(request))
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			return redirect('/index/')
		else:
			args['login_error'] = "error login/password"
			return render(request,'accounts/login.html', args)
	else:
		return render(request,'accounts/login.html', args)

def logout(request):
	auth.logout(request)
	return redirect('/main/')
