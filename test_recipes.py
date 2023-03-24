from functions.recipe_management import load_recipes_from_file
from functions.recipe_management import RecipeManagement
import unittest
import logging


class TestRecipes(unittest.TestCase):

    def test_non_existent_json_load_recipes(self):
        file_path = "data/test.txt"
        with self.assertRaises(Exception):
            load_recipes_from_file(file_path)

    def test_invalid_json_load_recipes(self):
        file_path = "data/recipes_test.json"
        with self.assertRaises(Exception):
            load_recipes_from_file(file_path)
    
    def test_valid_json_load_recipes(self):
        file_path = "data/recipes.json"

    def test_invalid_json_imported_recipes(self):
        file_path = "data/test_wrong_extension.pdf"
        with self.assertRaises(Exception):
            RecipeManagement.import_recipes(file_path)

    def test_empty_json_imported_recipes(self):
        file_path = "data/testrecipe_empty.json"
        with self.assertRaises(Exception):
            RecipeManagement.import_recipes(file_path)

    def test_add_recipe(self):
        recipe = {'name': 'Banana Milkshake', 'description': 'Thick and creamy Homemade Banana Milkshake recipe thats bursting with fresh banana flavor.', 'category': 'Drinks',
                    'rating': 5, 'image_url': 'https://foodtasia.com/wp-content/uploads/2021/07/banana-milkshake-40b-683x1024.jpg'}
        with self.assertRaises(Exception):
            RecipeManagement.add_recipe(recipe)
            
    def test_null_add_recipe(self):
        recipe = None
        with self.assertRaises(Exception):
            RecipeManagement.add_recipe(recipe)

    def test_edit_recipe(self):
        id = 2
        name = "Banana Milkshake" 
        description = "Thick and creamy Homemade Banana Milkshake recipe that’s bursting with fresh banana flavor."
        category = "Drinks"
        rating = 5
        image_url = "https://foodtasia.com/wp-content/uploads/2021/07/banana-milkshake-40b-683x1024.jpg"
        with self.assertRaises(Exception):
            RecipeManagement.edit_recipe(id, name, description, category, rating, image_url)

    def test_edit_nonexistant_recipe(self):
        id = 5
        name = "Banana Milkshake" 
        description = "Thick and creamy Homemade Banana Milkshake recipe that’s bursting with fresh banana flavor."
        category = "Drinks"
        rating = 5
        image_url = "https://foodtasia.com/wp-content/uploads/2021/07/banana-milkshake-40b-683x1024.jpg"
        with self.assertRaises(Exception):
            RecipeManagement.edit_recipe(id, name, description, category, rating, image_url)

