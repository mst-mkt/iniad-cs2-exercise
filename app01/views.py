from django.http import HttpRequest, HttpResponse


def root(_: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello Django")


def pattern(_: HttpRequest, username: str) -> HttpResponse:
    return HttpResponse(f"Hello {username}")


def param(request: HttpRequest) -> HttpResponse:
    text = ""
    for key in request.GET:
        text += f"{key} : {request.GET[key]}, "
    return HttpResponse(text)
