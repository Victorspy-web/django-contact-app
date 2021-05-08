from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm


#LIST, CREATE, READ, UPDATE and DELETE


#LIST
def contacts(request):
	contacts = Contact.objects.all()

	search_input = request.GET.get('search-area') or ''
	if search_input:
		contacts = Contact.objects.filter(firstName__icontains=search_input)

	context = {
		'contacts': contacts
	}

	return render(request, 'contacts.html', context)


#CREATE
def create_contact(request):
	form = ContactForm()

	if request.method == "POST":
		form = ContactForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('contacts')

	context = {
		'form' : form
	}

	return render(request, 'create_contact.html', context)


#READ
def contact_info(request, pk, *args, **Kwargs):
	contact = Contact.objects.get(id=pk)

	context = {
		'contact': contact
	}

	return render(request, 'contact.html', context)


#UPDATE
def contact_update(request, pk):
	contact = Contact.objects.get(id=pk)
	form = ContactForm(instance=contact)

	if request.method == "POST":
		form = ContactForm(request.POST, request.FILES, instance=contact)
		if form.is_valid():
			form.save()
			return redirect('contacts')

	context = {
		'contact' : contact,
		'form' : form,
	}

	return render(request, 'update.html', context)


#DELETE
def contact_delete(request, pk):
	contact = Contact.objects.get(id=pk)
	if request.method == "POST":
		contact.delete()
		return redirect('contacts')

	context = {
		'contact' : contact
	}

	return render(request, 'delete.html', context)

















