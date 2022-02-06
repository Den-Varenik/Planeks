from django.conf import settings
from django.db import models

from django.utils.translation import gettext_lazy as _
from model_utils import Choices


class Schema(models.Model):

    DELIMITER_CHOICES = Choices(
        (",", "comma", _("Comma (,)")),
        ("    ", "tab", _("Tab (    )")),
        (";", "semicolon", _("Semicolon (;)")),
        ("|", "pipe", _("Pipe (|)")),
    )

    QUOTE_CHOICES = Choices(
        ("\"", "double_quote", _("Double-quote (\")")),
        ("'", "quote", _("Quote (')")),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(_("Name"), max_length=32)
    delimiter = models.CharField(_("Column separator"), choices=DELIMITER_CHOICES, max_length=4)
    quote = models.CharField(_("String character"), choices=QUOTE_CHOICES, max_length=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)

    def get_absolute_url(self) -> str:
        pass


class Column(models.Model):

    TYPE_CHOICES = Choices(
        ("name", "name", _("Full name")),
        ("job", "job", _("Job")),
        ("email", "email", _("Email")),
        ("domain", "domain", _("Domain name")),
        ("phone", "phone", _("Phone number")),
        ("company", "company", _("Company name")),
        ("text", "text", _("Text")),
        ("number", "number", _("Integer")),
        ("address", "address", _("Address")),
        ("date", "date", _("Date")),
    )

    schema = models.ForeignKey(Schema, related_name="columns", on_delete=models.CASCADE)
    name = models.CharField(_("Column name"), max_length=100)
    type = models.CharField(_("Type"), choices=TYPE_CHOICES, max_length=20)
    range_from = models.IntegerField(_("From"), null=True)
    range_to = models.IntegerField(_("To"), null=True)
    order = models.IntegerField(_("Order"))

    def __str__(self):
        return f"{self.schema} -> {self.type}"
