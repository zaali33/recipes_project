from functions.recipe_management import load_recipes_from_file
from functions.recipe_management import RecipeManagement
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

    def test_empty_imported_file(self):
        file_path = "data/testrecipe_empty.json"
        test_result = RecipeManagement.import_recipes_for_test(self, file_path)
        self.assertFalse(test_result)

    def test_invalid_imported_file_extension(self):
        file_path = "data/test_wrong_extension.pdf"
        with self.assertRaises(Exception):
            RecipeManagement.import_recipes_for_test(self, file_path)

    def test_valid_imported_file(self):
        file_path = "data/sample_recipes.json"
        test_result = RecipeManagement.import_recipes_for_test(self, file_path)
        self.assertTrue(test_result, msg=None)

    def test_export_correct_file(self):
        file_path = "data/recipes.json"
        test_result = RecipeManagement.export_recipes_test(self, file_path)
        self.assertTrue(test_result, msg=None)