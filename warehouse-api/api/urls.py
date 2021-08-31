from django.urls import include, path

from rest_framework import routers

from .views import BookModelApi

router = routers.DefaultRouter()
router.register(r'books', BookModelApi)

urlpatterns = [
    path('', include(router.urls)),
]
