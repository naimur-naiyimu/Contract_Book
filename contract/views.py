from .models import Contract
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Contact
from django.shortcuts import render

def contract_list(request):
    contracts = Contract.objects.all()
    return render(request, 'contract_list.html', {'contracts': contracts})

def contract_add(request):
    if request.method == 'POST':
        # Add form processing logic here
        return HttpResponse('Contract added successfully!')
    else:
        # Render add contract form
        return render(request, 'add_contract.html')

def contract_update(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    if request.method == 'POST':
        # Update form processing logic here
        return HttpResponse('Contract updated successfully!')
    else:
        # Render update contract form
        return render(request, 'update_contract.html', {'contract': contract})

def contract_delete(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    # Delete contract logic here
    return HttpResponse('Contract deleted successfully!')