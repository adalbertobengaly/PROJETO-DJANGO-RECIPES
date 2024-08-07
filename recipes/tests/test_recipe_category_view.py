from django.urls import reverse, resolve
from recipes.views import site
from .test_recipe_base import RecipeTestBase


class RecipeCategoryViewTest(RecipeTestBase):

    def test_recipe_category_view_function_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        view = resolve(url)
        self.assertIs(view.func.view_class, site.RecipeListViewCategory)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        url = reverse('recipes:category', kwargs={'category_id': 1000})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'This is a category test'
        # Need a recipe for this test
        self.make_recipe(title=needed_title)

        url = reverse('recipes:category', args=(1,))
        response = self.client.get(url)
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_recipe_category_template_dont_load_recipes_not_published(self):
        """Test recipe when is_plublished is False dont show"""
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        url = reverse('recipes:recipe', kwargs={'pk': recipe.category.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
