from django.test import TestCase

from kitchen.forms import CookUpdateForm


class CookUpdateFormTests(TestCase):
    def setUp(self):
        self.valid_data = {
            "username": "testcook",
            "first_name": "John",
            "last_name": "Smith",
            "email": "john@example.com",
            "years_of_experience": 5,
        }

    def test_form_with_valid_data(self):
        form = CookUpdateForm(data=self.valid_data)

        self.assertTrue(form.is_valid())

    def test_username_cannot_be_empty(self):
        data = self.valid_data.copy()
        data["username"] = ""

        form = CookUpdateForm(data=data)

        self.assertFalse(form.is_valid())

    def test_first_name_can_be_empty(self):
        data = self.valid_data.copy()
        data["first_name"] = ""

        form = CookUpdateForm(data=data)

        self.assertTrue(form.is_valid())

    def test_last_name_can_be_empty(self):
        data = self.valid_data.copy()
        data["last_name"] = ""

        form = CookUpdateForm(data=data)

        self.assertTrue(form.is_valid())

    def test_email_can_be_empty(self):
        data = self.valid_data.copy()
        data["email"] = ""

        form = CookUpdateForm(data=data)

        self.assertTrue(form.is_valid())

    def test_years_of_experience_cannot_be_empty(self):
        data = self.valid_data.copy()
        data["years_of_experience"] = ""

        form = CookUpdateForm(data=data)

        self.assertFalse(form.is_valid())

    def test_years_of_experience_cannot_be_negative(self):
        data = self.valid_data.copy()
        data["years_of_experience"] = -1

        form = CookUpdateForm(data=data)

        self.assertFalse(form.is_valid())

    def test_email_should_have_valid_format(self):
        data = self.valid_data.copy()
        data["email"] = "not-an-email"

        form = CookUpdateForm(data=data)

        self.assertFalse(form.is_valid())
