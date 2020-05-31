from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


class HomePageMenu(ClusterableModel):

    name = models.CharField(
        max_length=255)

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Menu Items'


class HomePage(Page):

    quote = RichTextField(
        blank=True)

    body = RichTextField(
        blank=True)

    menu = ParentalKey(
        HomePageMenu,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('quote', classname="full"),
        FieldPanel('body', classname="full"),
        FieldPanel('menu'),
    ]

    class Meta:
        verbose_name = 'Homepage'
        verbose_name_plural = 'Homepages'
