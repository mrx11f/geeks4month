from django.urls import path
from post import views


urlpatterns = [
    path("", views.index_view, name="index-page"),
    path("contacts/", views.contacts_view, name="contacts-page"),
    path("about/", views.about_view, name="about-page"),
]