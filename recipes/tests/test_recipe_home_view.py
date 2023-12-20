from django.urls import reverse, resolve
from recipes import views
from unittest.mock import patch

from .test_recipe_base import RecipeTestBase


class RecipeHomeViewTest(RecipeTestBase):

    def test_recipe_home_view_function_is_correct(self):
        url = reverse('recipes:home')
        view = resolve(url)
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_Ok(self):
        url = reverse('recipes:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        url = reverse('recipes:home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        url = reverse('recipes:home')
        response = self.client.get(url)
        self.assertIn(
            '<h1>No recipes found here 😮‍💨</h1>',
            response.content.decode('utf-8')
        )

    def test_recipe_home_template_loads_recipes(self):
        # Need a recipe for this test
        self.make_recipe()

        url = reverse('recipes:home')
        response = self.client.get(url)
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        self.assertIn('Recipe Title', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        """Test recipe when is_plublished is False dont show"""
        # Need a recipe for this test
        self.make_recipe(is_published=False)

        url = reverse('recipes:home')
        response = self.client.get(url)

        self.assertIn(
            '<h1>No recipes found here 😮‍💨</h1>',
            response.content.decode('utf-8')
        )

    def test_recipe_home_is_paginated(self):
        for i in range(8):
            kwargs = {
                'slug': f'slug{i}',
                'author_data': {'username': f'usr-{i}'}
            }
            self.make_recipe(**kwargs)

        with patch('recipes.views.PER_PAGE', new=3):
            url = reverse('recipes:home')
            response = self.client.get(url)
            recipes = response.context['recipes']
            paginator = recipes.paginator

            self.assertEqual(paginator.num_pages, 3)
            self.assertEqual(len(paginator.get_page(1)), 3)
            self.assertEqual(len(paginator.get_page(2)), 3)
            self.assertEqual(len(paginator.get_page(3)), 2)

    def test_invalid_page_query_uses_page_one(self):
        for i in range(8):
            kwargs = {
                'slug': f'slug{i}',
                'author_data': {'username': f'usr-{i}'}
            }
            self.make_recipe(**kwargs)

        with patch('recipes.views.PER_PAGE', new=3):
            url = reverse('recipes:home')
            response = self.client.get(url + '?page=1A')
            self.assertEqual(
                response.context['recipes'].number,
                1
            )

            response = self.client.get(url + '?page=2')
            self.assertEqual(
                response.context['recipes'].number,
                2
            )

            response = self.client.get(url + '?page=3')
            self.assertEqual(
                response.context['recipes'].number,
                3
            )
