import random

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

weathers = ["Sunny", "Rainy", "Cloudy"]


def index(request: HttpRequest) -> HttpResponse:
    params: dict[str, str] = {}
    params["title"] = "3 days forecast"
    params["forecasts"] = random.choice(weathers)
    return render(request, "forecast/index.html", params)
