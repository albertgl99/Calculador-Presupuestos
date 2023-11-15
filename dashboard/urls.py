from django.urls import path

from . import views

urlpatterns = [
    path("", views.base, name="base"),
    path("calculate_price_view/", views.calculate_price_view, name='calculate_price_view'),
    path("generate_pdf/", views.generate_pdf, name='generate_pdf'),

] 