from selenium.webdriver.common.by import By
import pytest
from .base import RecipeBaseFunctionalTestCase


@pytest.mark.functional_test
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTestCase):
    def test_recipe_home_page_with_recipes_not_found_message(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('No recipes found here 😮‍💨', body.text)
