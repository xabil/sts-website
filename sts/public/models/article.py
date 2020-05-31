from django.db import models
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel,
                                         MultiFieldPanel)
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable, Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class ArticleIndexPage(Page):

    description = RichTextField(
        blank=True
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+')

    subpage_types = [
        'Article',
    ]

    search_fields = Page.search_fields + [
        index.SearchField('description'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
        ImageChooserPanel('image'),
    ]

    class Mera:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class ArticlePageTag(TaggedItemBase):

    content_object = ParentalKey(
        'Article',
        related_name='tagged_items',
        on_delete=models.CASCADE)


class Article(Page):

    author = models.CharField(
        max_length=1024,
        null=True,
        blank=True)

    published = models.DateField(
        'Post Date')

    intro = RichTextField(
        blank=True)

    body = RichTextField()

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+')

    tags = ClusterTaggableManager(
        through=ArticlePageTag,
        blank=True)

    @property
    def get_tags(self):
        return self.tags.all()

    parent_page_types = [
        ArticleIndexPage,
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('published'),
            FieldPanel('tags'),
        ], heading="Article information"),
        FieldPanel('author'),
        FieldPanel('intro', classname='full'),
        FieldPanel('body', classname='full'),
        ImageChooserPanel('image'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class ArticlePageGalleryImage(Orderable):

    page = ParentalKey(
        Article,
        on_delete=models.CASCADE,
        related_name='gallery_images')

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )

    caption = models.CharField(
        blank=True,
        max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
