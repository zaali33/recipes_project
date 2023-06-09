from flask import Flask
from flask_restful import Api
from resources.main_menu import MainMenu
from resources.recipes_crud import Recipes, RecipeDelete, RecipesEdit
from resources.recipes_crud import RecipesImport, Recipes_export
from resources.recipes_crud import RecipeAdd


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yrwejnfsdbflsdfs22'
api = Api(app)

api.add_resource(MainMenu, "/")
api.add_resource(Recipes, "/recipes")
api.add_resource(Recipes_export, "/recipes_export")
api.add_resource(RecipesImport, "/import")
api.add_resource(RecipeDelete, "/delete_recipe")
api.add_resource(RecipeAdd, "/add-recipe")
api.add_resource(RecipesEdit, "/edit", "/edit/<int:id>")

if __name__ == '__main__':
    app.run()
