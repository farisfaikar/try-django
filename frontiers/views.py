"""
> "What is your purpose?"
> "Render HTML web pages"
> "Fuck"
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from inventory.models import Inventory


def home_view(request, *args, **kwargs):
    """
    > Takes request (Django sent them)
    > Returns HTML as a response (We pick what to return for the response)
    > ???
    > profit
    """
    name = "Muhammad Sumbul"  # hard coded like your head
    number = random.randint(69, 420)  # API call to some bullshit rest API with python
    random_id = random.randint(1, 5)

    # From database? Yes dumbass
    inventory_obj = Inventory.objects.get(id=random_id)
    inventory_queryset = Inventory.objects.all()  # this returns a queryset (shortened to qs)

    arabic_cats = [
        "Ya'qub Qamar Ad-Din Dibiazah",
        "Khalid Kashmiri",
        "Khidir Karawita",
        "Ismail Ahmad Kanabawi",
        "Usman Abdul Jalil Sisha",
        "Muhammad Sumbul",
    ]

    context = {
        "object": inventory_obj,
        "id": inventory_obj.id,
        "title": inventory_obj.title,
        "content": inventory_obj.content,
        "name": name,
        "number": number,
        "arabic_cats": arabic_cats,
        "object_list": inventory_queryset,
        "important_number": inventory_obj.important_number,
    }

    # Django Template
    HTML_STRING = render_to_string("home-view.html", context=context)
    
    return HttpResponse(HTML_STRING)
