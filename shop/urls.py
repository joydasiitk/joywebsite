from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="Aboutshop"),
    path("contact/", views.contact, name="Contact Us"),
    path("tracker/", views.tracker, name="Tracking Status"),
    path("search/", views.search, name="Search"),
    path("productview/", views.productView, name="Productview"),
    path("checkout/", views.checkout, name="Check out")
]