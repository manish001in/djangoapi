from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from REST import views
from REST.views import DetailViewSet, UserViewSet
#from REST.views import api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
import logging
from django.views.static import serve
from newApp import settings

router = DefaultRouter()
router.register(r'detail', views.DetailViewSet)
router.register(r'users', views.UserViewSet)
logger = logging.getLogger(__name__)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^login/', include('rest_framework.urls', namespace='rest_framework')),
]


# rest_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# rest_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# rest_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
#
# urlpatterns = format_suffix_patterns([
#     url(r'^$', views.api_root),
#     url(r'^code/$',
#         rest_list,
#         name='rest-list'),
#     url(r'^code/(?P<pk>[0-9]+)/$',
#         rest_detail,
#         name='rest-detail'),
#     url(r'^code/(?P<pk>[0-9]+)/highlight/$',
#         rest_highlight,
#         name='rest-highlight'),
#     url(r'^users/$',
#         user_list,
#         name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$',
#         user_detail,
#         name='user-detail')
# ])

