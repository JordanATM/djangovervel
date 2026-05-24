from django.urls import path

from .views import static_home

urlpatterns = [
    path("", static_home, name="item-list"),
]
