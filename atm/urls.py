from django.urls import path

from atm.views import index, debit

urlpatterns = [
    path("", index, name="index"),
    path("debit", debit, name="debit"),
]