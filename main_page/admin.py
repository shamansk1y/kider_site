from django.contrib import admin
from .models import Team, Slider

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_editable = ['name', 'position', 'is_visible', 'profession', 'image']
    list_display = ['name', 'position', 'is_visible', 'profession', 'image']
    list_display_links = None


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    model = Slider
    list_editable = ['title', 'position', 'image', 'is_visible', 'h_1', 'desc', 'tab_1', 'tab_1_url', 'tab_2', 'tab_2_url']
    list_display = ['title', 'position', 'image', 'is_visible', 'h_1', 'desc', 'tab_1', 'tab_1_url', 'tab_2', 'tab_2_url']
    list_display_links = None
