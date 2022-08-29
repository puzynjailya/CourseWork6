from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.filters import AdsFilter
from ads.models import Advertisement
from ads.serializers import AdvertisementViewSerializer, AdvertisementDetailSerializer
from users.permissions import IsOwner, IsAdmin


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementViewSerializer
    pagination_class = AdPagination
    permission_classes = [AllowAny, ]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdsFilter

    def perform_create(self, serializer):
        user_data = self.request.get("user", None)
        serializer.save(author=user_data)

    def get_serializer_class(self, *args, **kwargs):
        if self.action in ['list']:
            return AdvertisementViewSerializer
        return AdvertisementDetailSerializer

    def get_queryset(self):
        if self.action == 'me':
            return Advertisement.objects.filter(author=self.request.user).all()
        return Advertisement.objects.all()

    def get_permissions(self):
        permission_classes = [AllowAny, ]
        if self.action in ['create', 'retrieve', 'update', 'delete', 'me']:
            permission_classes = [IsAuthenticated | IsOwner | IsAdmin]
        return tuple(permission() for permission in permission_classes)

    @action(detail=False, methods=['get',])
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


