"""
> "What is your purpose?"
> "Render HTML web pages"
> "Fuck"
"""
import random
from django.http import HttpResponse


def home_view(request):
    """
    > Takes request (Django sent them)
    > Returns HTML as a response (We pick to return the response)
    > ???
    > profit
    """
    name = "Muhammad Sumbul"
    number = random.randint(69, 420)  # API call to some rest API with python
    TITLE_STRING = "<title>CAPYBARA</title>"
    BODY_STRING = f"""
        <h1>OK I PULL UP</h1>
        <p>New player entered the game: {name}</p>
        <p>Random number, cause fuck you that's why: {number}</p>
    """
    HTML_STRING = TITLE_STRING + BODY_STRING
    return HttpResponse(HTML_STRING)
