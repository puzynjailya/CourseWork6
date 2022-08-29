from django.urls import include, path
from rest_framework_nested.routers import NestedSimpleRouter

from ads.urls import ads_router
from reviews.views import CommentViewSet

comments_router = NestedSimpleRouter(parent_router=ads_router, parent_prefix=r'ads', lookup='ad')
comments_router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
        path('', include(comments_router.urls)),
            ]
