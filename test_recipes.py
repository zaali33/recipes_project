from functions.recipe_management import load_recipes_from_file
import unittest

class TestRecipes(unittest.TestCase):

    def test_non_existent_json_load_recipes(self):
        file_path = "data/test.txt"
        with self.assertRaises(Exception):
            load_recipes_from_file(file_path)
    
    def test_invalid_json_load_recipes(self):
        file_path = "data/recipes_test.json"
        with self.assertRaises(Exception):
            load_recipes_from_file(file_path)
