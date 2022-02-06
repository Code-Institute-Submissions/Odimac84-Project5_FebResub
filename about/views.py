from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Testimonial, Contact
from .forms import TestimonialForm, ContactForm
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from profiles.models import UserProfile


def about_view(request):
    model = Testimonial
    form = TestimonialForm()
    template = 'about/about.html'

    testimonials = Testimonial.objects.all()

    paginator = Paginator(testimonials, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'form': form,
        'testimonials': testimonials,
        'page_obj': page_obj,
    }

    return render(request, template, context)


def contact_view(request):
    model = Contact
    form = ContactForm()
    template = 'about/contact.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


def create_contact(request):
    if request.method == "POST":
        contact = Contact()
        contact.title = request.POST.get('title')
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.question = request.POST.get('question')
        contact.telephone = request.POST.get('telephone')
        contact.save()
        _send_confirmation_email(contact)
        return redirect('home')


def _send_confirmation_email(contact):
    """Send confirmation email to user"""
    template_subject = 'about/confirmation_emails/confirmation_email_subject.txt'
    template_body = 'about/confirmation_emails/confirmation_email_body.txt'
    contact_email = settings.DEFAULT_FROM_EMAIL
    subject = render_to_string(template_subject, {'contact': contact})
    body = render_to_string(template_body, {'contact': contact})
    send_mail(subject, body, contact_email, [contact_email])


@login_required
def create_testimonial(request):
    if request.method == "POST":
        UserProfile.objects.get(user=request.user)
        feedback = Testimonial()
        feedback.name = request.user
        feedback.image = request.POST.get('image')
        feedback.rating = request.POST.get('rating')
        feedback.content = request.POST.get('content')
        feedback.save()
        return redirect('home')
