import random

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

weathers = ["Sunny", "Rainy", "Cloudy"]


def index(request: HttpRequest) -> HttpResponse:
    params: dict[str, str | list[str]] = {}
    params["title"] = "3 days forecast"
    params["forecasts"] = random.choices(weathers, k=7)
    return render(request, "forecast/index.html", params)
