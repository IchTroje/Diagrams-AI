from django.http import HttpResponse

def index(req):
    return  HttpResponse("<h1>Hello here :)</h1>")