from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from kitchen.models import DishType


def index(request):
    return render(request, "kitchen/index.html")


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dish_types"
    template_name = "kitchen/dish_type_list.html"