from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductQuerySet(models.QuerySet):
    def featured(self):
        return self.filter(is_featured=True)

    def category(self, slug):
        return self.filter(category__slug=slug)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def featured(self):
        return self.get_queryset().featured()

    def category(self, slug):
        return self.get_queryset().category(slug)


class Product(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.SET_DEFAULT, default=1)
    tags = models.ManyToManyField(Tag, blank=True)
    discount_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='products/')
    short_description = models.TextField(max_length=500, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    is_featured = models.BooleanField(default=False, blank=True, null=True)
    weight = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    length = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    breath = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    @property
    def get_price(self):
        if self.discount_price:
            return self.discount_price
        return self.price

    @property
    def saving(self):
        return self.discount_price - self.price

    @property
    def imageURL(self):
        if self.image:
            return self.image.url
        return ''
