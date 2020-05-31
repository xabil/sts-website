from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.search import index


class LinkGroup(models.Model):

    name = models.CharField(
        max_length=1024)

    description = RichTextField(
        blank=True)

    search_fields = [
        index.SearchField('description'),
    ]

    panels = [
        FieldPanel('name', classname='title'),
        FieldPanel('description', classname='full'),
    ]


class Link(models.Model):

    group = models.ForeignKey(
        LinkGroup,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    text = models.CharField(
        max_length=1024)

    link = models.URLField()

    email = models.EmailField(
        null=True,
        blank=True)

    search_fields = [
        index.SearchField('text'),
    ]

    panels = [
        FieldPanel('group'),
        FieldPanel('text'),
        FieldPanel('link'),
        FieldPanel('email'),
    ]

    def __str__(self):
        return self.text
