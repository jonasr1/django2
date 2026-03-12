from smtplib import SMTPException

from django.contrib import messages
from django.core.mail import BadHeaderError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from django2.forms import ContactForm


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


def contact(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.send_email()
            except (BadHeaderError, SMTPException, OSError):
                messages.error(request, "Error sending email!")
            else:
                messages.success(request, "Email sent successfully!")
            return redirect("contact")
        messages.error(request, "Error sending email!")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})


def product(request: HttpRequest) -> HttpResponse:
    return render(request, "product.html")
