from django.contrib import admin
from django.urls import path
from . import constants
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("send_prompt/", views.send_prompt_to_llm, name="send_prompt_to_llm"),
]
