from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Dish, Ingredient


class DishTypeModelTest(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="Dish Type")

        self.assertEqual(str(dish_type), "Dish Type")


class IngredientModelTest(TestCase):
    def test_ingredient_str(self):
        ingredient = Ingredient.objects.create(name="Cheese")

        self.assertEqual(str(ingredient), "Cheese")


class DishModelTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Pizza")

        self.dish = Dish.objects.create(
            name="Margherita",
            description="Description",
            price=Decimal("100.00"),
            dish_type=self.dish_type,
        )

    def test_dish_str(self):
        self.assertEqual(str(self.dish), "Margherita")

    def test_dish_has_dish_type(self):
        self.assertEqual(self.dish.dish_type, self.dish_type)

    def test_dish_can_have_cooks(self):
        cook = get_user_model().objects.create_user(
            username="testcook",
            password="testpassword123",
            years_of_experience=5,
        )

        self.dish.cooks.add(cook)

        self.assertIn(cook, self.dish.cooks.all())

    def test_dish_can_have_ingredients(self):
        ingredient = Ingredient.objects.create(name="Cheese")

        self.dish.ingredients.add(ingredient)

        self.assertIn(ingredient, self.dish.ingredients.all())
