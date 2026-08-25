from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from kitchen.models import DishType, Dish, Cook


def index(request):
    return render(request, "kitchen/index.html")


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dish_types"
    template_name = "kitchen/dish_type_list.html"


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    context_object_name = "dishes"
    template_name = "kitchen/dish_list.html"


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    context_object_name = "dish"
    template_name = "kitchen/dish_detail.html"


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    context_object_name = "cooks"
    template_name = "kitchen/cook_list.html"


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    context_object_name = "cook"
    template_name = "kitchen/cook_detail.html"
