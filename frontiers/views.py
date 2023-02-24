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
    random_id = random.randint(1, 5)

    # From database? Yes dumbass
    inventory_obj = Inventory.objects.get(id=random_id)
    # inventory_title = inventory_obj.title  # bit redundant innitexi
    # inventory_content = inventory_obj.content

    inventory_queryset = Inventory.objects.all()  # this returns a queryset (shortened to qs)

    arabic_cats = [
        "Ya'qub Qamar Ad-Din Dibiazah",
        "Khalid Kashmiri",
        "Khidir Karawita",
        "Ismail Ahmad Kanabawi",
        "Usman Abdul Jalil Sisha",
        "Muhammad Sumbul",
    ]
    # arabic_cats_str = ""
    # for i, cat in enumerate(arabic_cats):
    #     arabic_cats_str += f"<li>Warrior #{i}: {cat}</li>"


    context = {
        "object": inventory_obj,
        "id": inventory_obj.id,
        "title": inventory_obj.title,
        "content": inventory_obj.content,
        "name": "Muhammad Sumbul",
        "number": number,
        "arabic_cats": arabic_cats,
        "object_list": inventory_queryset,
    }

    # Django Template
    HTML_STRING = render_to_string("home-view.html", context=context)

    # This could be useful, but not for beginners like thyself
    # template = get_template("home-view.html")
    # template_str = template.render(context=context)
    # This is more-less how Django Template works, which is pretty cool. But we don't do that here
    # fucking = open("my-arse.html", 'r')
    # strink = fucking.read()
    # HTML_STRING = strink.format(**context)


    # HTML_STRING = """
    #     <title>{title}</title>
    #     <h1>OK I PULL UP</h1>
    #     <p>New player entered the game: {name}</p>
    #     <p>Random number, cause fuck you that's why: {number}</p>
    #     <h3>This data is pulled from my ass (id: {id})</h3>
    #     <p>Title: {title}</p>
    #     <p>Content: {content}</p>
    # """.format(**context)
    
    return HttpResponse(HTML_STRING)
