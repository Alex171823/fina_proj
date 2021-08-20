from django.urls import include, path

from rest_framework import routers

from .views import AuthorModelApi, AuthorBookMTMModelView, BookModelApi

router = routers.DefaultRouter()
router.register(r'authors', AuthorModelApi)
router.register(r'books', BookModelApi)
router.register(r'authorsbooks', AuthorBookMTMModelView)

urlpatterns = [
    path('', include(router.urls)),
]
