from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Category, Recipe, User


class RecipeViewTest(TestCase):
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
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='ussername',
            password='123456',
            email='username@email.com',
        )
        Recipe.objects.create(
            category=category,
            author=author,
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False,
            is_published=True,
        )

        url = reverse('recipes:home')
        response = self.client.get(url)
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        self.assertIn('Recipe Title', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('5 Porções', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_category_view_function_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        view = resolve(url)
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        url = reverse('recipes:category', kwargs={'category_id': 1000})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_function_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        view = resolve(url)
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipe_found(self):
        url = reverse('recipes:recipe', kwargs={'id': 1000})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
