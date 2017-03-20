from django.core.urlresolvers import reverse_lazy
from menu import Menu
from apps.main.menus import ViewMenuItem

# Administración
mye_children = (
    ViewMenuItem(
        "Cooperantes",
        reverse_lazy("cooperante_list"),
        weight=10,
        icon="fa-users"),
    ViewMenuItem(
        "Proyectos",
        reverse_lazy("proyecto_list"),
        weight=20,
        icon="fa-object-group"),
    ViewMenuItem(
        "Listado de solicitudes",
        reverse_lazy("solicitud_list"),
        weight=40,
        icon="fa-folder-open-o"),
    ViewMenuItem(
        "Listado de validaciones",
        reverse_lazy("validacion_list"),
        weight=50,
        icon="fa-check-square-o"),
    ViewMenuItem(
        "Informe",
        reverse_lazy("informe_mye"),
        weight=60,
        icon="fa-book"),)

Menu.add_item(
    "user",
    ViewMenuItem(
        "Evaluación",
        reverse_lazy('list_c'),
        weight=10,
        icon="fa-search",
        group="mye",
        children=mye_children))
