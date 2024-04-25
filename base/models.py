from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    validate_email,
    MaxValueValidator,
    MinValueValidator
)
from django.utils.translation import gettext_lazy as _

from base.enums import Gender
from hostel.models import TimedModel


class Users(AbstractUser, TimedModel):
    username = None
    middle_name = models.CharField(
        _("middle name"),
        max_length=50,
        null=True
    )
    email = models.EmailField(
        _("email address"),
        unique = True,
        error_messages = {
            "unique": _("A user with this email already exists."),
        },
        validators=[validate_email]
    )
    avatar = models.ImageField(
        _("profile pictire"),
        null=True
    )
    gender = models.CharField(
        _("gender"),
        max_length=10,
        choices=Gender.choices,
    )
    created_by = models.ForeignKey(
        'accommodation.Users',
        verbose_name=_("created by"),
        on_delete=models.SET_NULL,
        null=True,
        related_name="user_creator"
    )
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["firstname", "lastname", "password"]

    class Meta:
        ordering = TimedModel.Meta.ordering
        verbose_name = _("user")
        verbose_name_plural = _("users")


class Faculty(TimedModel):
    name = models.CharField(
        _("faculty name"),
        unique=True,
        max_length=50
    )

    class Meta:
        ordering = "name"
        verbose_name = _("faculty")
        verbose_name_plural = _("faculties")


class Department(TimedModel):
    name = models.CharField(
        _("department name"),
        unique=True,
        max_length=50
    )

    max_level = models.SmallIntegerField(
        _("maximum deparment level"),
        validators=[MinValueValidator(0), MaxValueValidator(7)]
    )

    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE,
        verbose_name=_("deparment faculty"),
        related_name="dept_faculty"
    )

    class Meta:
        ordering = "name"
        verbose_name = _("department")
        verbose_name_plural = _("departments")
