import dateutil.parser
from django.shortcuts import render
import requests

def index(request):
    yoko = requests.get('https://api.github.com/users/raybesiga')
    context = yoko.json()

    # context has a created_at key with a string value
    # parse the string value into a python date object
    context['created_at'] = dateutil.parser.parse(context['created_at'])
    return render(request, 'yokogao/index.html', context)
