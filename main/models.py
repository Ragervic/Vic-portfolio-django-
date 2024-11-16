from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


# Skill model
class Skill(models.Model):
    class Meta:
        verbose_name_plural = "Skills"
        verbose_name = "Skill"

    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=0, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# UserProfile model
class UserProfile(models.Model):
    class Meta:
        verbose_name_plural = "User Profiles"
        verbose_name = "User Profile"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(blank=True, null=True, max_length=200)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(upload_to="cv", blank=True, null=True)

    def _str_(self):
        return f"{self.user.first_name}{self.user.last_name}"


# Contactprofile model
class ContactProfile(models.Model):
    class Meta:
        verbose_name_plural = "Contact Profiles"
        verbose_name = "Contact Profile"
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f"{self.name}"


# Testimonial model
class Testimonial(models.Model):
    class Meta:
        verbose_name_plural = "Testimonials"
        verbose_name = "Testimonial"
        ordering = ["name"]

    thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonials")
    name = models.CharField(null=True, blank=True, max_length=200)
    role = models.CharField(null=True, blank=True, max_length=200)
    quote = models.CharField(null=True, blank=True, max_length=500)
    is_active = models.BooleanField(default=True)

    def _str_(self):
        return self.name


# Media model


class Media(models.Model):
    class Meta:
        verbose_name_plural = "Media Files"
        verbose_name = "Media"
        ordering = ["name"]

    image = models.ImageField(upload_to="media", blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
            super(Media, self).save(*args, **kwargs)

    def _str_(self):
        return self.name


# Portfolio model
class Portfolio(models.Model):
    class Meta:
        verbose_name_plural = "Portfolio Profiles"
        verbose_name = "Portfolio"
        ordering = ["name"]

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to="portfolio", blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def _str_(self):
        return self.name

    def get_absolute_Url(self):
        return f"/portfolio/{self.slug}"


# Blog model
class Blog(models.Model):
    class Meta:
        verbose_name_plural = "Blogs"
        verbose_name = "Blog"
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(blank=True, null=True, max_length=200)
    name = models.CharField(blank=True, null=True, max_length=200)
    description = models.CharField(blank=True, null=True, max_length=500)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
            super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"


# Certificate model
class Certificate(models.Model):
    class Meta:
        verbose_name_plural = "Certificates"
        verbose_name = "Certificate"

    name = models.CharField(blank=True, null=True, max_length=20)
    date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(blank=True, null=True, max_length=200)
    description = models.CharField(blank=True, null=True, max_length=500)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
