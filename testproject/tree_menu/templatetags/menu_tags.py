from django import template
from tree_menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html')
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')

    def build_menu_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent == parent:
                children = build_menu_tree(items, item)
                tree.append((item, children))

        return tree

    menu_tree = build_menu_tree(menu_items)

    return {'menu_tree': menu_tree}