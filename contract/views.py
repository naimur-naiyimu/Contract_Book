from .models import Contact
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Contact
from django.shortcuts import render

def Contact_list(request):
    Contacts = Contact.objects.all()
    return render(request, 'Contact_list.html', {'Contacts': Contacts})

def Contact_add(request):
    if request.method == 'POST':
        # Add form processing logic here
        return HttpResponse('Contact added successfully!')
    else:
        # Render add Contact form
        return render(request, 'add_Contact.html')

def Contact_edit(request, pk):
    Contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        # Update form processing logic here
        return HttpResponse('Contact updated successfully!')
    else:
        # Render update Contact form
        return render(request, 'update_Contact.html', {'Contact': Contact})

def Contact_delete(request, pk):
    Contact = get_object_or_404(Contact, pk=pk)
    # Delete Contact logic here
    return HttpResponse('Contact deleted successfully!')