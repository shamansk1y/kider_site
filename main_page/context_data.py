from .forms import MakeAppointmentForm, SubscriptionForm, ContactUsForm
from .models import Slider, Team, About, Testimonial, Classes, Facilities, Call, Gallery, Contacts, Schedule, Headlines


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
        'subscription': SubscriptionForm(),
        'contact_us': ContactUsForm(),
        'schedule': Schedule.objects.get(),
        'headlines': Headlines.objects.all(),
    }


def get_page_context(request):
    data = {
        'user_manager': request.user.groups.filter(name='manager').exists(),
        'user_auth': request.user.is_authenticated,
    }
    context = get_common_context()
    data.update(context)
    return data, context
