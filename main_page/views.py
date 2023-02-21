from django.shortcuts import render
from .models import Slider, Team, About, Testimonial, Classes, Facilities, Call, Gallery, Contacts

def index(request):
    slider = Slider.objects.filter(is_visible=True)
    team = Team.objects.all()[:3]
    about = About.objects.get()
    testimonial = Testimonial.objects.filter(is_visible=True)
    classes = Classes.objects.all().order_by('?')[:6]
    facilities = Facilities.objects.get()
    call = Call.objects.get()
    gallery = Gallery.objects.all().order_by('?')[:6]
    contacts = Contacts.objects.get()
    return render(
    request,
    'index.html', context={
    'slider': slider,
    'team': team,
    'about': about,
    'testimonial': testimonial,
    'classes': classes,
    'facilities': facilities,
    'call': call,
    'gallery': gallery,
    'contacts': contacts,
    })


def about(request):
    slider = Slider.objects.filter(is_visible=True)
    team = Team.objects.all()[:3]
    about = About.objects.get()
    testimonial = Testimonial.objects.filter(is_visible=True)
    classes = Classes.objects.all().order_by('?')[:6]
    facilities = Facilities.objects.get()
    call = Call.objects.get()
    gallery = Gallery.objects.all().order_by('?')[:6]
    contacts = Contacts.objects.get()
    return render(
    request,
    'about.html', context={
    'slider': slider,
    'team': team,
    'about': about,
    'testimonial': testimonial,
    'classes': classes,
    'facilities': facilities,
    'call': call,
    'gallery': gallery,
    'contacts': contacts,
    })