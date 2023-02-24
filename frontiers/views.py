"""
> "What is your purpose?"
> "Render HTML web pages"
> "Fuck"
"""
from django.http import HttpResponse

HTML_STRING = """
    <title>CAPYBARA</title>
    <h1>OK I PULL UP</h1>
"""


def home_view(request):
    """
    > Takes request (Django sent them)
    > Returns HTML as a response (We pick to return the response)
    > ???
    > profit
    """
    print(420 * 69)
    return HttpResponse(HTML_STRING)
