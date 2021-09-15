from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('shop_app.urls')),
    url(r'^cart/', include('cart.urls')),
]
