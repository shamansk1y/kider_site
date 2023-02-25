from django.shortcuts import render, redirect

from .context_data import get_common_context, get_page_context
from .forms import MakeAppointmentForm, SubscriptionForm, ContactUsForm
from .models import Subscription, ContactUs, Appointment
from django.contrib.auth.decorators import login_required, user_passes_test

def is_manager(user):
    return user.groups.filter(name='manager').exists()

def handle_post_request(request):

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
    if request.method == 'POST':
        handle_post_request(request)

    data, context = get_page_context(request)
    return render(request, 'index.html', context=data)

def about(request):
    if request.method == 'POST':
        handle_post_request(request)

    data, context = get_page_context(request)
    return render(request, 'about.html', context=data)

def contacts(request):
    if request.method == 'POST':
        handle_post_request(request)

    data, context = get_page_context(request)
    return render(request, 'contact.html', context=data)

def classes(request):
    if request.method == 'POST':
        handle_post_request(request)

    data, context = get_page_context(request)
    return render(request, 'classes.html', context=data)

def join_us(request):
    if request.method == 'POST':
        handle_post_request(request)

    data, context = get_page_context(request)
    return render(request, 'join_us.html', context=data)


def schedule(request):
    if request.method == 'POST':
        handle_post_request(request)

    data, context = get_page_context(request)
    return render(request, 'schedule.html', context=data)



@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_reservation(request, pk):
    Subscription.objects.filter(pk=pk).update(is_processed=True)
    ContactUs.objects.filter(pk=pk).update(is_processed=True)
    Appointment.objects.filter(pk=pk).update(is_processed=True)
    return redirect('main_page:list_reservations')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def list_reservation(request):
    subscription = Subscription.objects.filter(is_processed=False)
    contact_us = ContactUs.objects.filter(is_processed=False)
    make_appointment = Appointment.objects.filter(is_processed=False)
    return render(request, 'reservations.html', context={
        'subscription': subscription, 'make_appointment': make_appointment, 'contact_us': contact_us })