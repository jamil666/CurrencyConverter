from django.conf.urls import url
from .views import page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^', page)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
