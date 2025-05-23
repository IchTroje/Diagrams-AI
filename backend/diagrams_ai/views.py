from django.shortcuts import render
from django.http import JsonResponse
from .constants import LLM_CLIENT, BEFORE_PROMPT
import json


def index(request):
    return render(request, "diagrams_ai/base.html")


def send_prompt_to_llm(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            prompt = data.get("body", "").strip()

            if not prompt:
                return JsonResponse(
                    {"message": "Something went wrong with getting prompt to server"},
                    status=400,
                )

            completion = LLM_CLIENT.chat.completions.create(
                extra_body={},
                model="nvidia/llama-3.1-nemotron-ultra-253b-v1:free",
                messages=[{"role": "user", "content": BEFORE_PROMPT + prompt}],
            )
            return JsonResponse(
                {"message": f"{completion.choices[0].message.content}"}, safe=False
            )
        except json.JSONDecodeError:
            return JsonResponse({"message": "Wrong JSON format"}, status=400)

    return JsonResponse(
        {"message": "Other method HTTP method used, only POST works for this endpoint"},
        safe=False,
    )
