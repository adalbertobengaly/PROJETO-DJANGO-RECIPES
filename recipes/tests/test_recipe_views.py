from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipeViewTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        url = reverse('recipes:home')
        view = resolve(url)
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        view = resolve(url)
        self.assertIs(view.func, views.category)

    def test_recipe_detail_view_function_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        view = resolve(url)
        self.assertIs(view.func, views.recipe)

    def test_recipe_home_view_returns_status_code_200_Ok(self):
        url = reverse('recipes:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        url = reverse('recipes:home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
