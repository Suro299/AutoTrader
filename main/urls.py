from django.urls import path
from . import views

urlpatterns = [
   path("", views.garage, name = "garage"),
   path("detail_tuning/", views.detail_tuning, name = "detail_tuning"),
   path("car_tuning/<int:id>", views.car_tuning, name = "car_tuning"),
   path("buy_from_dealer", views.but_from_dealer, name = "bfd")
]



