from django.shortcuts import render
from eshop_settings.models import SiteSetting
from .models import ContactUS
from eshop_contact.forms import ContactForm


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')
        ContactUS.objects.create(full_name=full_name, email=email, subject=subject, text=text)
        # todo : show user a success message
        contact_form = ContactUS.objects.create()

    site_setting = SiteSetting.objects.first()
    context = {
        'contact_form':contact_form,
        'setting':site_setting
    }
    return render(request, 'contact_us.html', context)
