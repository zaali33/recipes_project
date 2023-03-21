from flask_restful import Resource
from flask import Response, render_template, request
from functions.recipe_management import RecipeManagement, Recipe


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

class RecipeAdd(Resource):
    def get(self):
        return Response(response=render_template("add-recipe.html"))
    
    def post(self):
        recipe = Recipe(id,name=request.form['recipeName'],
                        #   ingredients=request.form['recipeIngredients'],
                          description=request.form['recipeInstructions'],
                          category=request.form['recipeCategory'],
                          rating=request.form['recipeRating'],
                          image_url=request.form['recipeImage'])

        recipe_management = RecipeManagement()
        result = recipe_management.add_recipe(recipe)
        return Response(response=render_template("added-success.html", result = result))