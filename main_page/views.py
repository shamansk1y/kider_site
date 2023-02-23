from django.shortcuts import render, redirect
from .forms import MakeAppointmentForm, SubscriptionForm, ContactUsForm
from .models import Slider, Team, About, Testimonial, Classes, Facilities, Call, Gallery, Contacts


def get_common_context():
    """
    Return a dictionary containing common context data used in multiple views.

    Returns:
        A dictionary containing common context data used in multiple views.
    """
    return {
        'slider': Slider.objects.filter(is_visible=True),
        'team': Team.objects.all()[:3],
        'about': About.objects.get(),
        'testimonial': Testimonial.objects.filter(is_visible=True),
        'classes': Classes.objects.all().order_by('?')[:6],
        'facilities': Facilities.objects.get(),
        'call': Call.objects.get(),
        'gallery': Gallery.objects.all().order_by('?')[:6],
        'contacts': Contacts.objects.get(),
        'make_appointment': MakeAppointmentForm(),
        'subscription': SubscriptionForm(),
        'contact_us': ContactUsForm(),
    }

def handle_post_request(request):
    """
    Handle a POST request.

    Args:
        request: The HTTP request object.

    Returns:
        A redirect response if the form data is valid; otherwise, None.
    """
    make_appointment = MakeAppointmentForm(request.POST)
    contact_us = ContactUsForm(request.POST)
    subscription = SubscriptionForm(request.POST)

    if make_appointment.is_valid():
        make_appointment.save()
        return redirect('/')
    if contact_us.is_valid():
        contact_us.save()
        return redirect('/')
    if subscription.is_valid():
        subscription.save()
        return redirect('/')

def index(request):
    """
    Render the index page.

    Args:
        request: The HTTP request object.

    Returns:
        A response object that renders the index page with context data.
    """
    if request.method == 'POST':
        handle_post_request(request)

    context = get_common_context()
    return render(request, 'index.html', context=context)

def about(request):
    """
    Render the about page.

    Args:
        request: The HTTP request object.

    Returns:
        A response object that renders the about page with context data.
    """
    if request.method == 'POST':
        handle_post_request(request)

    context = get_common_context()
    return render(request, 'about.html', context=context)

def contacts(request):
    """
    Render the contacts page.

    Args:
        request: The HTTP request object.

    Returns:
        A response object that renders the contacts page with context data.
    """
    if request.method == 'POST':
        handle_post_request(request)

    context = get_common_context()
    return render(request, 'contact.html', context=context)

def classes(request):
    """
    Render the classes page.

    Args:
        request: The HTTP request object.

    Returns:
        A response object that renders the classes page with context data.
    """
    if request.method == 'POST':
        handle_post_request(request)

    context = get_common_context()
    return render(request, 'classes.html', context=context)

def join_us(request):
    """
    Render the join us page.

    Args:
        request: The HTTP request object.

    Returns:
        A response object that renders the join us page with context data.
    """
    if request.method == 'POST':
        handle_post_request(request)

    context = get_common_context()
    return render(request, 'join_us.html', context=context)
