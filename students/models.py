from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

from base.models import Department, Faculty, Users
from hall.models import Blocks, Hall, Rooms, Session
from hostel.models import TimedModel


class Student(TimedModel):
    matric_no = models.CharField(
        _("matriculation number"),
        max_length=6,
        validators=MinLengthValidator(6)
    )
    dob = models.DateTimeField(_("date of birth"))
    faculty = models.ForeignKey(
        Faculty,
        verbose_name=_("student faculty"),
        on_delete=models.PROTECT,
        related_name="student_faculty"
    )
    department = models.ForeignKey(
        Department,
        verbose_name=_("student department"),
        on_delete=models.PROTECT,
        related_name="student_department"
    )
    refrences = ArrayField(
        models.FileField(),
        verbose_name=_("accommodation"),
        size=2
    )
    auhority_to_pay = models.FileField(
        _("authoriity to pay")
    )
    jamb_form = models.FileField(
        _("jamb admission form")
    )
    user = models.ForeignKey(
        Users,
        verbose_name=_("student users"),
        on_delete=models.CASCADE,
        related_name="student_user",
    )
    hall = models.ForeignKey(
        Hall,
        verbose_name=_("student hall"),
        on_delete=models.CASCADE,
        related_name="student_hall"
    )

    class Meta:
        ordering = TimedModel.Meta.ordering
        verbose_name = _("student")
        verbose_name_plural = _("students")


class Application():
    student = models.ForeignKey(
        Student,
        verbose_name=_("student application"),
        on_delete=models.CASCADE,
        related_name="student_application"
    )
    session = models.ForeignKey(
        Session,
        verbose_name=_("application session"),
        on_delete=models.CASCADE,
        related_name="application_session"
    )
    block_prefrence = models.ForeignKey(
        Blocks,
        verbose_name=_("block prefrence"),
        on_delete=models.SET_NULL,
        related_name="application_block",
        null=True
    )
    room_prefrence = models.ForeignKey(
        Rooms,
        verbose_name=_("room prefrences"),
        on_delete=models.SET_NULL,
        related_name="application_room"
    )
    allocated_to = models.ForeignKey(
        Rooms,
        verbose_name=_("allocated to"),
        on_delete=models.PROTECT,
        related_name="allocated_room",
    )
    accepted_on = models.DateTimeField(
        _("application accepted on"),
        null=True
    )
    rejected_on = models.DateTimeField(
        _("application rejected on")
    )


class Issues(TimedModel):
    description = models.TextField(
        _("Issue Description")
    )
    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name="application issue",
    )
