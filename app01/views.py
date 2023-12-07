from django.http import HttpRequest, HttpResponse


def root(_: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello Django")
