from django.contrib import admin
from .models import Testimonial, Contact


class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'testimonal_date_on',
        'rating',
        'content',
        'image',
        'approved',
    )

    ordering = ('testimonal_date_on',)


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'title',
        'question',
        'telephone',
        'asked_date',
    )

    ordering = ('asked_date',)


admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Contact, ContactAdmin)
