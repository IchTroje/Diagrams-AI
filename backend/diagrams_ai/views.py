from django.shortcuts import render


def index(request):
    return render(request, "diagrams_ai/base.html")
