from django.contrib import admin
from .models import Team, Slider, About, Testimonial, Classes

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_editable = ['name', 'position', 'is_visible', 'profession', 'image', 'image_clas']
    list_display = ['name', 'position', 'is_visible', 'profession', 'image', 'image_clas']
    list_display_links = None


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    model = Slider
    list_editable = ['title', 'position', 'image', 'is_visible', 'h_1', 'desc', 'tab_1', 'tab_1_url', 'tab_2', 'tab_2_url']
    list_display = ['title', 'position', 'image', 'is_visible', 'h_1', 'desc', 'tab_1', 'tab_1_url', 'tab_2', 'tab_2_url']
    list_display_links = None

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    model = About
    list_editable = ['h1', 'desc', 'tab', 'user', 'pos_user', 'img_user', 'is_visible', 'img_1', 'img_2', 'img_3']
    list_display = ['h1', 'desc', 'tab', 'user', 'pos_user', 'img_user', 'is_visible', 'img_1', 'img_2', 'img_3']
    list_display_links = None

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    model = Testimonial
    list_editable = ['name', 'position', 'is_visible', 'profession', 'image', 'desc']
    list_display = ['name', 'position', 'is_visible', 'profession', 'image', 'desc']
    list_display_links = None

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    model = Classes
    list_editable = ['title', 'price', 'is_visible', 'position', 'image', 'teacher']
    list_display = ['title', 'price', 'is_visible', 'position', 'image', 'teacher']
    list_display_links = None

