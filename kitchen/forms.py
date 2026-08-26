from django import forms
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import Cook, Dish, DishType, Ingredient


class CookCreationForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        ]


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        ]


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = [
            "name",
            "description",
            "price",
            "dish_type",
            "cooks",
            "ingredients",
        ]


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name",]
