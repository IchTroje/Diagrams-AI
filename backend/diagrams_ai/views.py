from django.shortcuts import render
from django.http import JsonResponse
import json


def index(request):
    return render(request, "diagrams_ai/base.html")


def send_prompt_to_llm(request):
    if request.method == "POST":
        prompt = json.loads(request.body.decode("utf-8"))["body"]
        return JsonResponse({"message": f"{prompt}"}, safe=False)
    return JsonResponse({"message": "Wszystko jest git :)"}, safe=False)
