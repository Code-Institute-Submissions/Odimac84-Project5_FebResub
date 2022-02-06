from django import forms
from .models import Testimonial, Contact

# form for customer to leave a testimonial for site
class TestimonialForm(forms.ModelForm):

    class Meta:
        model = Testimonial
        fields = ('rating', 'content', 'image')

        name = forms.CharField,
        rating = forms.IntegerField,
        content = forms.Textarea,

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# form for customer to contact in case they want
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

        name = forms.CharField,
        email = forms.EmailField,
        title = forms.CharField,
        question = forms.Textarea,
        telephone = forms.CharField,

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)