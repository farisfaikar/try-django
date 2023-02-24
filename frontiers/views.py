"""
> "What is your purpose?"
> "Render HTML web pages"
> "Fuck"
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from inventory.models import Inventory


def home_view(request):
    """
    > Takes request (Django sent them)
    > Returns HTML as a response (We pick to return the response)
    > ???
    > profit
    """
    name = "Muhammad Sumbul"  # hard coded like your head
    number = random.randint(69, 420)  # API call to some bullshit rest API with python

    # From database? Yes dumbass
    inventory_obj = Inventory.objects.get(id=2)
    # inventory_title = inventory_obj.title  # bit redundant innitexi
    # inventory_content = inventory_obj.content

    arabic_cats = [
        "Ya'qub Qamar Ad-Din Dibiazah",
        "Khalid Kashmiri",
        "Khidir Karawita",
        "Ismail Ahmad Kanabawi",
        "Usman Abdul Jalil Sisha",
        "Our Lord Muhammad Sumbul",
    ]
    arabic_cats_str = ""
    for x in arabic_cats:
        arabic_cats_str += f"Number is {x}\n"


    context = {
        "id": inventory_obj.id,
        "title": inventory_obj.title,
        "content": inventory_obj.content,
        "name": "Muhammad Sumbul",
        "number": number,
        "arabic_cats_str": arabic_cats_str,
    }

    # Django Template
    
    # This is more-less how Django Template works, which is pretty cool. But we don't do that here
    fucking = open("my-arse.html", 'r')
    strink = fucking.read()
    HTML_STRING = strink.format(**context)


    HTML_STRING = """
        <title>{title}</title>
        <h1>OK I PULL UP</h1>
        <p>New player entered the game: {name}</p>
        <p>Random number, cause fuck you that's why: {number}</p>
        <h3>This data is pulled from my ass (id: {id})</h3>
        <p>Title: {title}</p>
        <p>Content: {content}</p>
    """.format(**context)
    
    return HttpResponse(HTML_STRING)
