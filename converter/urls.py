from django.conf.urls import url
from .views import page

urlpatterns = [

    url(r'^', page)
]

