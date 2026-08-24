from django.urls import path

from kitchen import views


app_name = "kitchen"

urlpatterns = [
    path("", views.index, name="index"),
]
