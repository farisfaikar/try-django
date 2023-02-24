from django.shortcuts import render

from .models import Inventory

# Create your views here.
def inventory_detail_view(request, id=None):
    inventory_obj = None
    if id is not None:
        inventory_obj = Inventory.objects.get(id=id)
    context = {
        "object": inventory_obj,
    }
    return render(request, "inventory/detail.html", context=context)
    