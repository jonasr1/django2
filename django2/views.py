from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, "contact.html")


def product(request: HttpRequest) -> HttpResponse:
    return render(request, "product.html")
