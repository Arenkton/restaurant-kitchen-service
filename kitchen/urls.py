from django.urls import path

from kitchen import views


app_name = "kitchen"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "types/",
        views.DishTypeListView.as_view(),
        name="dish-type-list",
    ),
    path(
        "types/create/",
        views.DishTypeCreateView.as_view(),
        name="dish-type-create",
    ),
    path(
        "types/<int:pk>/update/",
        views.DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "types/<int:pk>/delete/",
        views.DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
    path(
        "dishes/",
        views.DishListView.as_view(),
        name="dish-list",
    ),
    path(
        "dishes/<int:pk>/",
        views.DishDetailView.as_view(),
        name="dish-detail",
    ),
    path(
        "dishes/create/",
        views.DishCreateView.as_view(),
        name="dish-create",
    ),
    path(
        "dishes/<int:pk>/update/",
        views.DishUpdateView.as_view(),
        name="dish-update",
    ),
    path(
        "cooks/",
        views.CookListView.as_view(),
        name="cook-list",
    ),
    path(
        "cooks/<int:pk>/",
        views.CookDetailView.as_view(),
        name="cook-detail",
    ),
]
