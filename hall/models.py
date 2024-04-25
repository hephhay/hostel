from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import Users
from hostel.models import TimedModel


class Management(TimedModel):
    position = models.CharField(
        _("position"),
        max_length=30,
    )
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name="management_user"
    )


class Session(TimedModel):
    name = models.CharField(
        _("session name"),
        unique=True,
        max_length=10
    )



class Hall(TimedModel):
    name = models.CharField(
        _("hall name"),
        unique=True,
        max_length=30
    )
    slogan = models.TextField(
        _("hall slogan"),
        null=True
    )
    avatar = models.FileField(
        _("hall logo"),
    )


class Blocks(TimedModel):
    name = models.CharField(
        _("black name"),
        max_length=1
    )


class Rooms(TimedModel):
    number = models.IntegerField(
        _("room number"),
        validators=MinValueValidator(0)
    )
    allocatable = models.BooleanField(
        _("room allocatable"),
        default=True
    )
    max_no_in_room = models.SmallIntegerField(
        _("maximum number of students in room"),
        validators=[MinValueValidator(0), MaxValueValidator(7)]
    )
