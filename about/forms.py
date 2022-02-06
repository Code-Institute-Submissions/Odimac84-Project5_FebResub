from django import forms
from .models import Testimonial, Contact

# form for customer to leave a testimonial for site
class TestimonialForm(forms.ModelForm):

    class Meta:
        model = Testimonial
        fields = ('rating', 'content', 'image')
        # choices = (
        #     ('1', '1'),
        #     ('2', '2'),
        #     ('3', '3'),
        #     ('4', '4'),
        #     ('5', '5'),
        # )

        name = forms.CharField,
        rating = forms.ChoiceField(choices=[(x, x) for x in range(1, 5)]),
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