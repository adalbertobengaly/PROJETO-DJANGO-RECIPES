from django.urls import reverse, resolve
from recipes.views import site
from .test_recipe_base import RecipeTestBase


class RecipeDetailViewTest(RecipeTestBase):

    def test_recipe_detail_view_function_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'pk': 1})
        view = resolve(url)
        self.assertIs(view.func.view_class, site.RecipeDetail)

    def test_recipe_detail_view_returns_404_if_no_recipe_found(self):
        url = reverse('recipes:recipe', kwargs={'pk': 1000})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_the_correct_recipe(self):
        needed_title = 'This is a detail page - It load one recipe'
        # Need a recipe for this test
        self.make_recipe(title=needed_title)

        url = reverse('recipes:recipe', kwargs={'pk': 1})
        response = self.client.get(url)
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_recipe_detail_template_dont_load_recipes_not_published(self):
        """Test recipe when is_plublished is False dont show"""
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        url = reverse('recipes:recipe', kwargs={'pk': recipe.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
