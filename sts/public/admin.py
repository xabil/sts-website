from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from public.models.home import HomePageMenu
from public.models.link import Link, LinkGroup


class LinkAdmin(ModelAdmin):
    """
    Link admin
    """

    model = Link
    menu_label = 'Links'
    menu_icon = 'link'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("group", "text",)
    search_fields = ("group", "text",)


class LinkGroupAdmin(ModelAdmin):
    """
    Link Group admin
    """

    model = LinkGroup
    menu_label = 'Link Groups'
    menu_icon = 'link'
    menu_order = 290
    add_to_settings_menu = True
    exclude_from_explorer = False
    list_display = ("name",)
    search_fields = ("name",)


class MenuAdmin(ModelAdmin):
    """
    Menu admin
    """

    model = HomePageMenu
    menu_label = 'Menus'
    menu_icon = 'snippet'
    menu_order = 290
    add_to_settings_menu = True
    exclude_from_explorer = False
    list_display = ("name",)
    search_fields = ("name",)


modeladmin_register(LinkAdmin)
modeladmin_register(LinkGroupAdmin)
modeladmin_register(MenuAdmin)
