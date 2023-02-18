from django.shortcuts import render
from .models import Slider, Team

def index(request):
    slider = Slider.objects.filter(is_visible=True)
    team = Team.objects.filter(is_visible=True)

    return render(
        request,
        'index.html', context={
     'slider': slider,
     'team': team,
    })