from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    params = {}
    params["title"] = "3 days forecast"
    return render(request, "forecast/index.html", params)
