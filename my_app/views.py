from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Plumbing, Biodigester, WaterTreatment, SolarInstallation, ContactMessage

def index(request):
    return render(request, "index.html")

def biodigester(request):
    biodigesters = Biodigester.objects.all()
    return render(request, "biodigester.html", {'biodigesters': biodigesters})

def plumbing(request):
    plumbing_items = Plumbing.objects.all()
    return render(request, "plumbing.html", {'plumbing_items': plumbing_items})

def water(request):
    water_treatments = WaterTreatment.objects.all()
    return render(request, "water.html", {'water_treatments': water_treatments})

def solar(request):
    solar_installations = SolarInstallation.objects.all()
    return render(request, "solar.html", {'solar_installations': solar_installations})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to the database
        contact_message = ContactMessage(name=name, email=email, message=message)
        contact_message.save()

        try:
            # Send email
            full_message = f"Message from {name} ({email}):\n\n{message}"
            send_mail(
                subject=f"Contact form submission from {name}",
                message=full_message,
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],  # Your email address
                fail_silently=False,
            )
            
            # Display a success message
            messages.success(request, 'Your message was sent successfully!')

        except Exception as e:
            # Display an error message
            messages.error(request, f'Error sending message: {e}')

        return redirect('contact')

    return render(request, 'contact.html')
