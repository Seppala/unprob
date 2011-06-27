from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from splash.models import Entry
from django.template import RequestContext
from splash.forms import EntryForm

	
def createEntry(request):

	if request.method == 'POST': # If the form has been submitted...
		form = EntryForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			new_entry = form.save()			
			return HttpResponseRedirect('success/') # Redirect after POST
	else:
		form = EntryForm() # An unbound form
	variables = RequestContext(request, { 'form': form })
	return render_to_response('splash/index.html', variables)
	#return render_to_response('test.html')
	
def success(request):
	return render_to_response('splash/success.html')
def about(request):
	return render_to_response('splash/about.html')
def team(request):
	return render_to_response('splash/team.html')
def contact(request):
	return render_to_response('splash/contact.html')
		
	
#def createEntry(request):
	
#	if request.method == 'POST': # If the form has been submitted...
#		form = EntryForm(request.POST) # A form bound to the POST data
#		if form.is_valid(): # All validation rules pass
#			new_entry = form.save()			
#			return HttpResponseRedirect('splash/success.html') # Redirect after POST
#	else:
#		form = EntryForm() # An unbound form
#		variables = RequestContext(request, { 'form': form })
#		return render_to_response('/', variables)