from django.shortcuts import render
from .models import Slider, Team, About, Testimonial, Classes

def index(request):
    slider = Slider.objects.filter(is_visible=True)
    team = Team.objects.all()[:3]
    about = About.objects.get()
    testimonial = Testimonial.objects.filter(is_visible=True)
    classes = Classes.objects.all()[:6]

    return render(
    request,
    'index.html', context={
    'slider': slider,
    'team': team,
    'about': about,
    'testimonial': testimonial,
    'classes': classes,
    })