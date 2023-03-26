from functions.recipe_management import load_recipes_from_file
from functions.recipe_management import RecipeManagement, Recipe
import unittest
import logging
import json


class TestRecipes(unittest.TestCase):

    ''' test cases of load_recipes_from_file '''

    def test_non_existent_json_load_recipes(self):
        file_path = "data/test.txt"
        with self.assertRaises(Exception):
            load_recipes_from_file(file_path)

    def test_invalid_json_load_recipes(self):
        file_path = "data/recipes_test.json"
        with self.assertRaises(Exception):
            load_recipes_from_file(file_path)

    def test_valid_json_load_recipes(self):
        file_path = "data/recipes_copy.json"
        recipes_data = [{"id": 1, "name": "Mix Berry Smoothie", "description": "A delicious and healthy blended drink made from a variety of fresh or frozen berries", "category": "desserts", "rating": 5, "image_url": "https://www.jessicagavin.com/wp-content/uploads/2020/07/berry-smoothie-8-1200.jpg"}, {"id": 2,
                                                                                                                                                                                                                                                                                                                "name": "Frozen Yogurt Bark", "description": "A tasty and healthy snack that is made from a base of creamy yogurt, typically Greek yogurt, and frozen fruit. ", "category": "desserts", "rating": 4, "image_url": "https://www.notenoughcinnamon.com/wp-content/uploads/2021/03/Healthy-Frozen-Yogurt-Bark-3-500x500.jpg"}]
        recipes_loaded_data = load_recipes_from_file(file_path)
        self.assertEqual(recipes_loaded_data, recipes_data)

    ''' test cases of view_recipes '''

    def test_view_recipes(self):
        recipe_management = RecipeManagement()
        file_path = "data/recipes_copy.json"
        recipes_loaded_data = load_recipes_from_file(file_path)
        recipes_view_data = recipe_management.view_recipes()
        self.assertEqual(recipes_loaded_data, recipes_view_data)

    ''' test cases of filter_recipes '''

    def test_filter_by_name_recipes(self):
        recipe_management = RecipeManagement()
        name = "Berr"
        recipes_filtered_data = recipe_management.filter_recipes(name, "", "")
        recipes_expected = [{"id": 1, "name": "Mix Berry Smoothie", "description": "A delicious and healthy blended drink made from a variety of fresh or frozen berries",
                             "category": "desserts", "rating": 5, "image_url": "https://www.jessicagavin.com/wp-content/uploads/2020/07/berry-smoothie-8-1200.jpg"}]
        self.assertEqual(recipes_expected, recipes_filtered_data)

    def test_filter_by_category_recipes(self):
        recipe_management = RecipeManagement()
        category = "desserts"
        recipes_filtered_data = recipe_management.filter_recipes(
            "", category, "")
        recipes_expected = [{"id": 1, "name": "Mix Berry Smoothie", "description": "A delicious and healthy blended drink made from a variety of fresh or frozen berries", "category": "desserts", "rating": 5, "image_url": "https://www.jessicagavin.com/wp-content/uploads/2020/07/berry-smoothie-8-1200.jpg"}, {"id": 2,
                                                                                                                                                                                                                                                                                                                    "name": "Frozen Yogurt Bark", "description": "A tasty and healthy snack that is made from a base of creamy yogurt, typically Greek yogurt, and frozen fruit. ", "category": "desserts", "rating": 4, "image_url": "https://www.notenoughcinnamon.com/wp-content/uploads/2021/03/Healthy-Frozen-Yogurt-Bark-3-500x500.jpg"}]
        self.assertEqual(recipes_expected, recipes_filtered_data)

    def test_filter_by_rating_recipes(self):
        recipe_management = RecipeManagement()
        rating = 4
        recipes_filtered_data = recipe_management.filter_recipes(
            "", "", rating)
        recipes_expected = [{"id": 2, "name": "Frozen Yogurt Bark", "description": "A tasty and healthy snack that is made from a base of creamy yogurt, typically Greek yogurt, and frozen fruit. ",
                             "category": "desserts", "rating": 4, "image_url": "https://www.notenoughcinnamon.com/wp-content/uploads/2021/03/Healthy-Frozen-Yogurt-Bark-3-500x500.jpg"}]
        self.assertEqual(recipes_expected, recipes_filtered_data)

    def test_filter_by_string_rating_recipes(self):
        recipe_management = RecipeManagement()
        rating = "4"
        recipes_filtered_data = recipe_management.filter_recipes(
            "", "", rating)
        recipes_expected = [{"id": 2, "name": "Frozen Yogurt Bark", "description": "A tasty and healthy snack that is made from a base of creamy yogurt, typically Greek yogurt, and frozen fruit. ",
                             "category": "desserts", "rating": 4, "image_url": "https://www.notenoughcinnamon.com/wp-content/uploads/2021/03/Healthy-Frozen-Yogurt-Bark-3-500x500.jpg"}]
        self.assertEqual(recipes_expected, recipes_filtered_data)

    def test_filter_by_non_existent_category_recipes(self):
        recipe_management = RecipeManagement()
        category = "blah"
        recipes_filtered_data = recipe_management.filter_recipes(
            "", category, "")
        recipes_expected = []
        self.assertEqual(recipes_expected, recipes_filtered_data)

    def test_filter_by_non_existent_name_recipes(self):
        recipe_management = RecipeManagement()
        name = "blah"
        recipes_filtered_data = recipe_management.filter_recipes(name, "", "")
        recipes_expected = []
        self.assertEqual(recipes_expected, recipes_filtered_data)

    def test_filter_by_non_existent_ratings(self):
        recipe_management = RecipeManagement()
        rating = 7
        recipes_filtered_data = recipe_management.filter_recipes(
            "", "", rating)
        recipes_expected = []
        self.assertEqual(recipes_expected, recipes_filtered_data)

    def test_filter_by_None_ratings(self):
        recipe_management = RecipeManagement()
        rating = None
        recipes_filtered_data = recipe_management.filter_recipes(
            "", "", rating)
        recipes_expected = [{"id": 1, "name": "Mix Berry Smoothie", "description": "A delicious and healthy blended drink made from a variety of fresh or frozen berries", "category": "desserts", "rating": 5, "image_url": "https://www.jessicagavin.com/wp-content/uploads/2020/07/berry-smoothie-8-1200.jpg"}, {"id": 2,
                                                                                                                                                                                                                                                                                                                    "name": "Frozen Yogurt Bark", "description": "A tasty and healthy snack that is made from a base of creamy yogurt, typically Greek yogurt, and frozen fruit. ", "category": "desserts", "rating": 4, "image_url": "https://www.notenoughcinnamon.com/wp-content/uploads/2021/03/Healthy-Frozen-Yogurt-Bark-3-500x500.jpg"}]
        self.assertEqual(recipes_expected, recipes_filtered_data)

    def test_filter_by_all_fields(self):
        recipe_management = RecipeManagement()
        rating = 4
        name = "yogurt"
        category = "desserts"
        recipes_filtered_data = recipe_management.filter_recipes(
            name, category, rating)
        recipes_expected = [{"id": 2, "name": "Frozen Yogurt Bark", "description": "A tasty and healthy snack that is made from a base of creamy yogurt, typically Greek yogurt, and frozen fruit. ",
                             "category": "desserts", "rating": 4, "image_url": "https://www.notenoughcinnamon.com/wp-content/uploads/2021/03/Healthy-Frozen-Yogurt-Bark-3-500x500.jpg"}]
        self.assertEqual(recipes_expected, recipes_filtered_data)

    ''' test cases of get_recipe '''

    def test_get_valid_recipe(self):
        recipe_management = RecipeManagement()
        recipe_id = 2
        recipes_expected = {"id": 2, "name": "Frozen Yogurt Bark", "description": "A tasty and healthy snack that is made from a base of creamy yogurt, typically Greek yogurt, and frozen fruit. ",
                            "category": "desserts", "rating": 4, "image_url": "https://www.notenoughcinnamon.com/wp-content/uploads/2021/03/Healthy-Frozen-Yogurt-Bark-3-500x500.jpg"}
        recipe = recipe_management.get_recipe(recipe_id)
        self.assertEqual(recipes_expected, recipe)

    def test_get_not_found_recipe(self):
        recipe_management = RecipeManagement()
        recipe_id = 4
        recipes_expected = None
        recipe = recipe_management.get_recipe(recipe_id)
        self.assertEqual(recipes_expected, recipe)

    def test_get_invalid_recipe(self):
        recipe_management = RecipeManagement()
        recipe_id = "blah"
        recipes_expected = None
        recipe = recipe_management.get_recipe(recipe_id)
        self.assertEqual(recipes_expected, recipe)

    ''' test cases of delete_recipe '''

    def test_invalid_delete_recipe(self):
        recipe_management = RecipeManagement()
        recipe_id = 4
        with self.assertRaises(Exception):
            recipe_management.delete_recipe(recipe_id)

    def test_valid_delete_recipe(self):
        recipe_management = RecipeManagement()
        recipe_id = 1
        recipes_expected = [{"id": 2, "name": "Frozen Yogurt Bark", "description": "A tasty and healthy snack that is made from a base of creamy yogurt, typically Greek yogurt, and frozen fruit. ",
                             "category": "desserts", "rating": 4, "image_url": "https://www.notenoughcinnamon.com/wp-content/uploads/2021/03/Healthy-Frozen-Yogurt-Bark-3-500x500.jpg"}]
        recipe_management.delete_recipe(recipe_id)
        recipes = recipe_management.view_recipes()
        self.assertEqual(recipes_expected, recipes)
        # put the recipes.json file back to its original form
        recipes_original = load_recipes_from_file("data/recipes_copy.json")
        with open('data/recipes.json', 'w') as f:
            json.dump({"recipes": recipes_original}, f)

    ''' test cases of Import and Export File '''

    def test_invalid_imported_file_extension(self):
        file_path = "data/test_wrong_extension.pdf"
        with self.assertRaises(Exception):
            RecipeManagement.import_recipes(self,file_path)

    def test_valid_import(self):
        file_path = "fakerecipes.json"
        test_result = RecipeManagement.import_recipes(self,file_path)
        self.assertTrue(test_result,msg=None)

    def test_empty_import(self):
        file_path = "testrecipe_empty.json"

        test_result = RecipeManagement.import_recipes(self, file_path)
        self.assertFalse(test_result, msg=None)

    def test_export(self):
        with self.assertRaises(Exception):
            RecipeManagement.export_recipes(self)

    def test_add_recipe(self):
        recipe = Recipe(id,
                        name="Banana Milkshake",
                        description="Thick and creamy Homemade Banana Milkshake recipe that’s bursting with fresh banana flavor.",
                        category="Drinks",
                        rating=5,
                        image_url="https://foodtasia.com/wp-content/uploads/2021/07/banana-milkshake-40b-683x1024.jpg"
                        )
        test_result = RecipeManagement.add_recipe(self, recipe)
        self.assertTrue(test_result, msg=None)
        recipes_original = load_recipes_from_file("data/recipes_copy.json")
        with open('data/recipes.json', 'w') as f:
            json.dump({"recipes": recipes_original}, f)

    def test_null_add_recipe(self):
        recipe = None
        with self.assertRaises(Exception):
            RecipeManagement.add_recipe(recipe)

    def test_edit_recipe(self):
        recipe_management = RecipeManagement()
        recipes_expected = [{
            "id": 1,
            "name": "Mix Berry Smoothie",
            "description": "A delicious and healthy blended drink made from a variety of fresh or frozen berries",
            "category": "desserts",
            "rating": 5,
            "image_url": "https://www.jessicagavin.com/wp-content/uploads/2020/07/berry-smoothie-8-1200.jpg"
        },
            {
            "id": 2,
            "name": "Banana Milkshake",
            "description": "Thick and creamy Homemade Banana Milkshake recipe that’s bursting with fresh banana flavor.",
            "category": "Drinks",
            "rating": 5,
            "image_url": "https://foodtasia.com/wp-content/uploads/2021/07/banana-milkshake-40b-683x1024.jpg"
        }]
        id = 2
        name = "Banana Milkshake"
        description = "Thick and creamy Homemade Banana Milkshake recipe that’s bursting with fresh banana flavor."
        category = "Drinks"
        rating = 5
        image_url = "https://foodtasia.com/wp-content/uploads/2021/07/banana-milkshake-40b-683x1024.jpg"
        recipe_management.edit_recipe(id, name, description, category, rating, image_url)      
        recipes = recipe_management.view_recipes()
        self.assertEqual(recipes_expected, recipes)
        recipes_original = load_recipes_from_file("data/recipes_copy.json")
        with open('data/recipes.json', 'w') as f:
            json.dump({"recipes": recipes_original}, f)

    def test_edit_nonexistant_recipe(self):
        id = 5
        name = "Banana Milkshake"
        description = "Thick and creamy Homemade Banana Milkshake recipe that’s bursting with fresh banana flavor."
        category = "Drinks"
        rating = 5
        image_url = "https://foodtasia.com/wp-content/uploads/2021/07/banana-milkshake-40b-683x1024.jpg"
        with self.assertRaises(Exception):
            RecipeManagement.edit_recipe(
                id, name, description, category, rating, image_url)
