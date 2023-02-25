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
    

def inventory_search_view(request):
    print(dir(request))
    print(request.GET)
    query_dick = request.GET  # this is a dicktionary
    query = query_dick.get("q")  # <input type='text' name='q'/>

    try:
        query = str(query_dick.get("q"))
    except:
        query = None
    
    inventory_obj = None
    if query is not None:
        inventory_obj = Inventory.objects.get(title=query)
    context = {
        "object": inventory_obj,
    }
    return render(request, "inventory/search.html", context=context)