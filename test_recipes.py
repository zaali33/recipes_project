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

