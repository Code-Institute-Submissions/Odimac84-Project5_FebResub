from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Testimonial(models.Model):
    choices = (
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
        )

    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="testimonial")
    testimonal_date_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=3, choices=choices)
    content = models.TextField(max_length=1000)
    image = models.ImageField(null=True, blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['testimonal_date_on']

    def __str__(self):
        return f"{self.name.username} gave a rating of {self.rating}"


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    title = models.CharField(max_length=50)
    question = models.TextField(max_length=5000)
    telephone = models.CharField(max_length=20)
    asked_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['asked_date']

    def __str__(self):
        return f"{self.name} asked a question on{self.asked_date}"
