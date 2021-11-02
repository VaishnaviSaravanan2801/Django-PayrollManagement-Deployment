from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth


def index(request):
	if request.user.is_authenticated:
		return redirect("/dashboard")
		
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			messages.success(request, "Your are now logged in")
			return redirect("/dashboard")
		else:
			messages.error(request, "Invalid credentials")
			return redirect("login")

	else:
		return render(request, "login.html")


def logout(request):
	auth.logout(request)
	messages.success(request, 'Your are now logged out')
	return redirect('login')
