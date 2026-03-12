from django import forms
from django.conf import settings
from django.core.mail import EmailMessage


class ContactForm(forms.Form):
    subject = forms.CharField(label="Subject", max_length=120)
    message = forms.CharField(label="Message", widget=forms.Textarea())
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def send_email(self) -> int:
        sender = self.cleaned_data["sender"]
        subject = self.cleaned_data["subject"]
        message = self.cleaned_data["message"]
        cc_myself = self.cleaned_data["cc_myself"]
        body = f"Sender: {sender}\n\n{message}"
        mail = EmailMessage(
            subject=subject,
            body=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.CONTACT_EMAIL],
            cc=[sender] if cc_myself else None,
            reply_to=[sender],
        )
        return mail.send()
