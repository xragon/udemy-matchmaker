from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, RequestContext, Http404, HttpResponseRedirect
from django.forms.models import modelformset_factory


from .models import Address, Job, UserPicture 
from .forms import AddressForm, JobForm, UserPictureForm

def home(request):

	return render_to_response('home.html', locals(), context_instance=RequestContext(request))


def all(request):

	users = User.objects.filter(is_active=True)

	return render_to_response('profiles/all.html', locals(), context_instance=RequestContext(request))


def single_user(request, username):
	try:
		user = User.objects.get(username=username)
		if user.is_active:
			single_user = user
	except:
		raise Http404

	return render_to_response('profiles/single_user.html', locals(), context_instance=RequestContext(request))


def edit_profile(request):
	user = request.user
	
	try:
		addresses = Address.objects.filter(user=user)
	except:
		addresses = None

	#try:
	jobs = Job.objects.filter(user=user)
	#except:
	#	jobs = None

	#try:
	picture = UserPicture.objects.get(user=user)
	#except:
	#	picture = None
	

	#addresses = Address.objects.filter(user=user)
	#jobs = Job.objects.filter(user=user)
	#picture = UserPicture.objects.filter(user=user)

	AddressFormset = modelformset_factory(Address, form=AddressForm, extra=1)
	formset_a = AddressFormset(queryset=addresses)

	JobFormset = modelformset_factory(Job, form=JobForm, extra=1)
	formset_j = JobFormset(queryset=jobs)

	#address_form = AddressForm(request.POST or None, prefix='address', instance=addresses)
	#job_form = JobForm(request.POST or None, prefix='job', instance=jobs)
	picture_form = UserPictureForm(request.POST or None, request.FILES or None, prefix='pic', instance=picture)

	if picture_form.is_valid():
		form1 = address_form.save(commit=False)
		form1.save()
		form2 = job_form.save(commit=False)
		form2.save()
		form3 = picture_form.save(commit=False)
		form3.save()

	return render_to_response('profiles/edit_profile.html', locals(), context_instance=RequestContext(request))

def edit_address(request):
	if request.method == 'POST':
		user = request.user
		addresses = Address.objects.filter(user=user)

		AddressFormset = modelformset_factory(Address, form=AddressForm, extra=1)
		formset_a = AddressFormset(request.POST or None, queryset=addresses)

		if formset_a.is_valid():
			for form in formset_a:
				new_form = form.save(commit=False)
				new_form.user = request.user
				new_form.save()

			messages.success(request, 'Profile details updated.')
		else:
			messages.error(request, 'Profile detials update failed.')

		return HttpResponseRedirect('/edit/')

	else:
		raise Http404


def edit_job(request):
	if request.method == 'POST':
		user = request.user
		jobs = Job.objects.filter(user=user)

		JobFormset = modelformset_factory(Job, form=JobForm, extra=1)
		formset_j = JobFormset(request.POST or None, queryset=jobs)

		if formset_j.is_valid():
			for form in formset_j:
				new_form = form.save(commit=False)
				new_form.user = request.user
				new_form.save()

			messages.success(request, 'Profile details updated.')
		else:
			messages.error(request, 'Profile detials update failed.')

		return HttpResponseRedirect('/edit/')

	else:
		raise Http404