from django.contrib import admin

from .models import (
    Certificate,
    Blog,
    Portfolio,
    Testimonial,
    ContactProfile,
    UserProfile,
    Skill,
    Media,
)

# registering of the models


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user")


@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "timestamp", "name")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "score")


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    readonly_fields = ("slug",)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    readonly_fields = ("slug",)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
