"""
> "What is your purpose?"
> "Render HTML web pages"
> "Fuck"
"""
import random
from django.http import HttpResponse

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

    # Django Templates
    TITLE_STRING = f"<title>{inventory_obj.title}</title>"
    BODY_STRING = f"""
        <h1>OK I PULL UP</h1>
        <p>New player entered the game: {name}</p>
        <p>Random number, cause fuck you that's why: {number}</p>
        <h3>This data is pulled from my ass (id: {inventory_obj.id})</h3>
        <p>Title: {inventory_obj.title}</p>
        <p>Content: {inventory_obj.content}</p>
    """
    HTML_STRING = TITLE_STRING + BODY_STRING
    return HttpResponse(HTML_STRING)
