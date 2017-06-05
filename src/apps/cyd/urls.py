from django.conf.urls import url, include
from apps.cyd.views import *
from apps.cyd import api_views

from rest_framework.routers import DefaultRouter

cyd_router = DefaultRouter()
cyd_router.register(r'api/grupo', api_views.GrupoViewSet)
cyd_router.register(r'api/calendario', api_views.CalendarioViewSet)

urlpatterns = [
    url(r'^curso/add/$', CursoCreateView.as_view(), name='curso_add'),
    url(r'^curso/list/$', CursoListView.as_view(), name='curso_list'),
    url(r'^curso/(?P<pk>\d+)/$', CursoDetailView.as_view(), name='curso_detail'),

    url(r'^sede/add/$', SedeCreateView.as_view(), name='sede_add'),
    url(r'^sede/list/$', SedeListView.as_view(), name='sede_list'),
    url(r'^sede/(?P<pk>\d+)/$', SedeDetailView.as_view(), name='sede_detail'),
    url(r'^sede/(?P<pk>\d+)/editar$', SedeUpdateView.as_view(), name='sede_update'),

    url(r'^grupo/add/$', GrupoCreateView.as_view(), name='grupo_add'),
    url(r'^grupo/list/$', GrupoListView.as_view(), name='grupo_list'),
    url(r'^grupo/(?P<pk>\d+)/$', GrupoDetailView.as_view(), name='grupo_detail'),

    url(r'', include(cyd_router.urls)),
]
