from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType, Ingredient


class PublicViewTests(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="testcook",
            password="testpassword123",
            years_of_experience=5,
        )

        self.dish_type = DishType.objects.create(
            name="Pizza",
        )

        self.dish = Dish.objects.create(
            name="Margherita",
            description="Classic pizza",
            price=10.50,
            dish_type=self.dish_type,
        )

    def test_login_required_for_index(self):
        url = reverse("kitchen:index")
        response = self.client.get(url)

        self.assertNotEqual(response.status_code, 200)

    def test_login_required_for_dish_type_list(self):
        url = reverse("kitchen:dish-type-list")
        response = self.client.get(url)

        self.assertNotEqual(response.status_code, 200)

    def test_login_required_for_dish_list(self):
        url = reverse("kitchen:dish-list")
        response = self.client.get(url)

        self.assertNotEqual(response.status_code, 200)

    def test_login_required_for_dish_detail(self):
        url = reverse(
            "kitchen:dish-detail",
            kwargs={"pk": self.dish.pk},
        )
        response = self.client.get(url)

        self.assertNotEqual(response.status_code, 200)

    def test_login_required_for_cook_list(self):
        url = reverse("kitchen:cook-list")
        response = self.client.get(url)

        self.assertNotEqual(response.status_code, 200)

    def test_login_required_for_cook_detail(self):
        url = reverse(
            "kitchen:cook-detail",
            kwargs={"pk": self.cook.pk},
        )
        response = self.client.get(url)

        self.assertNotEqual(response.status_code, 200)

    def test_login_required_for_ingredient_list(self):
        url = reverse("kitchen:ingredient-list")
        response = self.client.get(url)

        self.assertNotEqual(response.status_code, 200)


class PrivateViewTests(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="testcook",
            password="testpassword123",
            years_of_experience=5,
        )
        self.client.force_login(self.cook)

        self.dish_type = DishType.objects.create(
            name="Pizza",
        )

        self.ingredient = Ingredient.objects.create(
            name="Cheese",
        )

        self.dish = Dish.objects.create(
            name="Margherita",
            description="Classic pizza",
            price=10.50,
            dish_type=self.dish_type,
        )

    def test_index_view(self):
        response = self.client.get(
            reverse("kitchen:index")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "kitchen/index.html",
        )

    def test_dish_type_list_view(self):
        response = self.client.get(
            reverse("kitchen:dish-type-list")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "kitchen/dish_type_list.html",
        )
        self.assertIn(
            self.dish_type,
            response.context["dish_types"],
        )

    def test_dish_list_view(self):
        response = self.client.get(
            reverse("kitchen:dish-list")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "kitchen/dish_list.html",
        )
        self.assertIn(
            self.dish,
            response.context["dishes"],
        )

    def test_dish_detail_view(self):
        response = self.client.get(
            reverse(
                "kitchen:dish-detail",
                kwargs={"pk": self.dish.pk},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "kitchen/dish_detail.html",
        )
        self.assertEqual(
            response.context["dish"],
            self.dish,
        )

    def test_cook_list_view(self):
        response = self.client.get(
            reverse("kitchen:cook-list")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "kitchen/cook_list.html",
        )
        self.assertIn(
            self.cook,
            response.context["cooks"],
        )

    def test_cook_detail_view(self):
        response = self.client.get(
            reverse(
                "kitchen:cook-detail",
                kwargs={"pk": self.cook.pk},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "kitchen/cook_detail.html",
        )
        self.assertEqual(
            response.context["cook"],
            self.cook,
        )

    def test_ingredient_list_view(self):
        response = self.client.get(
            reverse("kitchen:ingredient-list")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "kitchen/ingredient_list.html",
        )
        self.assertIn(
            self.ingredient,
            response.context["ingredients"],
        )
