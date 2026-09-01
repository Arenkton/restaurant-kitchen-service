from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType, Ingredient


class SearchTests(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="chef_john",
            password="testpassword123",
            first_name="John",
            last_name="Smith",
            years_of_experience=5,
        )
        self.client.force_login(self.cook)

        self.dish_type = DishType.objects.create(
            name="Italian",
        )

        self.dish = Dish.objects.create(
            name="Margherita Pizza",
            description="Classic pizza",
            price=10.50,
            dish_type=self.dish_type,
        )

        self.ingredient = Ingredient.objects.create(
            name="Mozzarella",
        )

    def test_search_dish_by_name(self):
        response = self.client.get(
            reverse("kitchen:dish-list"),
            {"q": "Margherita"},
        )

        self.assertContains(response, self.dish.name)

    def test_search_dish_type_by_name(self):
        response = self.client.get(
            reverse("kitchen:dish-type-list"),
            {"q": "Italian"},
        )

        self.assertContains(response, self.dish_type.name)

    def test_search_ingredient_by_name(self):
        response = self.client.get(
            reverse("kitchen:ingredient-list"),
            {"q": "Mozzarella"},
        )

        self.assertContains(response, self.ingredient.name)

    def test_search_cook_by_username(self):
        response = self.client.get(
            reverse("kitchen:cook-list"),
            {"q": "chef_john"},
        )

        self.assertContains(response, self.cook.username)

    def test_search_cook_by_first_name(self):
        response = self.client.get(
            reverse("kitchen:cook-list"),
            {"q": "John"},
        )

        self.assertContains(response, self.cook.username)

    def test_search_cook_by_last_name(self):
        response = self.client.get(
            reverse("kitchen:cook-list"),
            {"q": "Smith"},
        )

        self.assertContains(response, self.cook.username)

    def test_search_returns_no_unmatched_dishes(self):
        response = self.client.get(
            reverse("kitchen:dish-list"),
            {"q": "Sushi"},
        )

        self.assertNotContains(response, self.dish.name)
