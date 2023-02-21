from django.contrib import admin
from .models import Team, Slider, About, Testimonial, Classes, Facilities, Call, Gallery, Contacts, Appointment


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


@admin.register(Facilities)
class FacilitiesAdmin(admin.ModelAdmin):
    model = Facilities
    list_editable = ['h1_col_1', 'desc_col_1', 'position', 'is_visible', 'h1_col_2', 'desc_col_2',
                     'h1_col_3', 'desc_col_3', 'h1_col_4', 'desc_col_4']
    list_display = ['h1_col_1', 'desc_col_1', 'position', 'is_visible', 'h1_col_2', 'desc_col_2',
                    'h1_col_3', 'desc_col_3', 'h1_col_4', 'desc_col_4']
    list_display_links = None


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    model = Call
    list_editable = ['title', 'position', 'image', 'is_visible', 'desc', 'tab_1', 'tab_1_url']
    list_display = ['title', 'position', 'image', 'is_visible', 'desc', 'tab_1', 'tab_1_url']
    list_display_links = None


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    model = Gallery
    list_editable = ['position', 'image', 'is_visible']
    list_display = ['position', 'image', 'is_visible']
    list_display_links = None


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    model = Contacts
    list_editable = ['h1', 'address', 'phone', 'email', 'twi_url', 'fb_url', 'youtube_url', 'in_url']
    list_display = ['h1', 'address', 'phone', 'email', 'twi_url', 'fb_url', 'youtube_url', 'in_url']
    list_display_links = None

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    model = Appointment
    list_editable = ['name', 'email', 'child_name', 'child_age', 'message', 'is_processed']
    list_display = ['name', 'email', 'child_name', 'child_age', 'message', 'date', 'date_processing', 'is_processed']
    list_display_links = None

