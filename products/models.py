from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    make = models.CharField(max_length=254, null=True, blank=True)
    model_id = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    # Model for review on products
    product = models.ForeignKey(
        Product, related_name="review", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    review = models.TextField(max_length=1000, null=False, blank=False)
    post_date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-post_date"]

    def __str__(self):
        return f"review {self.pk} by {self.author} on the {self.post_date}"
