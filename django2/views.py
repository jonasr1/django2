from smtplib import SMTPException

from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import BadHeaderError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from django2.forms import ContactForm, ProductModelForm
from django2.models import Product


def signup(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        return render(request, "registration/signup.html", {"form": UserCreationForm()})
    form = UserCreationForm(request.POST)
    if not form.is_valid():
        return render(request, "registration/signup.html", {"form": form})
    form.save()
    messages.success(request, "User created successfully!")
    return redirect("login")


def logout(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        auth_logout(request)
        return redirect("login")
    return render(request, "registration/logout.html")


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html", {"products": Product.objects.all()})


def _render_contact(request, form):  # noqa
    return render(
        request,
        "contact.html",
        {"title": "Contact", "form": form},
    )


def contact(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        return _render_contact(request, ContactForm())
    form = ContactForm(request.POST)
    if not form.is_valid():
        return render(request, form)
    try:
        form.send_email()
    except (BadHeaderError, SMTPException, OSError):
        messages.error(request, "Error sending email!")
        return redirect("contact")
    messages.success(request, "Email sent successfully!")
    return redirect("contact")


def _render_product(request, form):  # noqa
    return render(
        request,
        "product.html",
        {
            "title": "Product",
            "form": form,
            "enctype": "multipart/form-data",
            "submit_label": "Register",
        },
    )


@login_required
def product(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        return _render_product(request, ProductModelForm())
    form = ProductModelForm(request.POST, request.FILES)
    if not form.is_valid():
        messages.error(request, "Error saving product!")
        return _render_product(request, form)
    form.save()
    messages.success(request, "Product saved successfully!")
    return redirect("product")
