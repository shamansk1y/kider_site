from django import forms
from main_page.models import Appointment, Subscription


class MakeAppointmentForm(forms.ModelForm):
    name = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control border-0",
                'id': "gname",
                'placeholder': "Gurdian Name",
                }))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'type':"email",
                'class': "form-control border-0",
                'id': "gmail",
                'placeholder': "Gurdian Email"}))

    child_name = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.TextInput(
            attrs={'type': "text",
                    'class': "form-control border-0",
                    'id': "cname",
                    'placeholder': "Child Name"}))

    child_age = forms.CharField(
        max_length=2,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control border-0",
                'id': "cage",
                'placeholder': "Child Age"}))

    message = forms.CharField(
        max_length=250,
        widget=forms.Textarea(
            attrs={
                'class': "form-control border-0",
                'placeholder': "Leave a message here",
                'id': "message",
                'style': "height: 100px",
                "message": 'Message'}))

    class Meta:
        model = Appointment
        fields = ['name', 'email', 'child_name', 'child_age', 'message']


class SubscriptionForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': "form-control bg-transparent w-100 py-3 ps-4 pe-5",
                'type': "text",
                'placeholder': "Your email"
            }))
    class Meta:
        model = Subscription
        fields = ['email']