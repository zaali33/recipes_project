from flask_restful import Resource
from flask import Response, render_template
from functions.recipe_management import RecipeManagement


# view (get) and add (post) functions will be called in this class
class Recipes(Resource):
    def get(self):
        recipe_management = RecipeManagement()
        recipes = recipe_management.view_recipes()
        return Response(response=render_template("view.html", recipes=recipes))

class RecipesImport(Resource):
    def get(self):
        return Response(response=render_template("import-recipes.html"))

    def post(self):
        recipe_management = RecipeManagement()
        result = recipe_management.import_recipes()
        return Response(response=render_template("import-success.html", result = result))
