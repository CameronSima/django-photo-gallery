from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import settings

from paypal.standard.forms import PayPalPaymentsForm

from registration.backends.default.views import RegistrationView, ActivationView

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/")
	else:
		form = UserCreationForm()
	return render(request, "registration/register.html", {
		'form': form,
	})

@csrf_exempt
def front(request):
	return render(request, "front.html")

def contact(request):
	return render(request, "contact.html")

def about(request):
	return render(request, "about.html")

@login_required
def user_profile(request):
	return render(request, "registration/profile.html")

@csrf_exempt
def payment(request):

	"""
	This is the view for the page a new user is redirected
	to after registering (not activating) a new account.
	"""

	paypal_dict = {
		"cmd": "_xclick-subscriptions",
		"business": settings.PAYPAL_RECEIVER_EMAIL,
		"a3": "7.99",
		"p3": "1",
		"t3": "M",
		"src": "1",
		"sra": "1",
		"no_note": "1",
		"item_name": "S&B Photography",
		"notify_url": "https://ffb6262.ngrok.com/",
		"return_url": "https://ffb6262.ngrok.com/",
		"cancel_return": "https://ffb6262.ngrok.com/",
		
		
	}

	form = PayPalPaymentsForm(initial=paypal_dict, button_type="subscribe")
	context = {"form": form}
	return render_to_response("registration/registration_complete.html", context)



class CustomRegView(RegistrationView):
	""" 
	This is the view that handles new user registration.
	It is subclassed from registration/backends/default.RegistrationView.
	Instead of sending a confirmation email to activate the account,
	as is done in the registration default backend, I want paypal 
	payment to activate the account. 
	"""

	SEND_ACTIVATION_EMAIL = False

def paypal_incomin(request):
	if request.POST['Completed']:
		print 'yes'
	else:
		print request

from django.utils.html import escape
def paypal_incoming(request):
    print 'Something at least'




