from django.shortcuts import render
from django.http import JsonResponse
import json


def index(request):
    return render(request, "diagrams_ai/base.html")


def send_prompt_to_llm(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            prompt = data.get("body", "").strip()  # Zastosowanie .get() i usuwanie białych znaków

            if not prompt:  # Jeśli prompt jest pusty
                return JsonResponse({"message": "Proszę wprowadzić treść promptu."}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"message": "Niepoprawny format JSON"}, status=400)

        return JsonResponse({"message": prompt}, safe=False)

    return JsonResponse({"message": "Wszystko jest git :)"}, safe=False)
