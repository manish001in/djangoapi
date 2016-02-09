from REST.models import REST
from REST.serializers import RESTSerializer, UserSerializer
from rest_framework import generics, permissions, renderers, viewsets
from django.contrib.auth.models import User
from REST.permissions import IsOwnerOrReadOnly
import logging
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse


# @api_view(('GET',))
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'snippets': reverse('rest-list', request=request, format=format)
#     })


class DetailViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = REST.objects.all()
    serializer_class = RESTSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        logger = logging.getLogger(__name__)
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    logger = logging.getLogger(__name__)
    queryset = User.objects.all()
    serializer_class = UserSerializer
