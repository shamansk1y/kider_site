from django.shortcuts import render, redirect
from .forms import MakeAppointmentForm
from .models import Slider, Team, About, Testimonial, Classes, Facilities, Call, Gallery, Contacts


def get_common_context():
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
    }

def index(request):
    if request.method == 'POST':
        make_appointment = MakeAppointmentForm(request.POST)
        if make_appointment.is_valid():
            make_appointment.save()
            return redirect('/')

    context = get_common_context()
    return render(request, 'index.html', context=context)

def about(request):
    context = get_common_context()
    return render(request, 'about.html', context=context)

def contacts(request):
    context = get_common_context()
    return render(request, 'contact.html', context=context)

def classes(request):
    if request.method == 'POST':
        make_appointment = MakeAppointmentForm(request.POST)
        if make_appointment.is_valid():
            make_appointment.save()
            return redirect('classes')

    context = get_common_context()
    return render(request, 'classes.html', context=context)

def join_us(request):
    if request.method == 'POST':
        make_appointment = MakeAppointmentForm(request.POST)
        if make_appointment.is_valid():
            make_appointment.save()
            return redirect('/')

    context = get_common_context()
    return render(request, 'join_us.html', context=context)
