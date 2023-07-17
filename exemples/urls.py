from django.urls import path
from exemples import views

urlpatterns = [
    path("test/",views.test_view, name="test-view"),
    path("test/hello",views.test_view_hello, name="test-hello"),
    path("test/goodbye",views.test_view_bye, name="test-bye"),
    path("test/<int:number>",views.catch_number_view, name="catch_number"),
    path("test/<str:string>/test/",views.catch_string_view, name="catch_string"),
]