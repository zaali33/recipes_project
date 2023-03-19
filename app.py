from flask import Flask
from flask_restful import Api
from resources.main_menu import MainMenu
from resources.recipes_crud import Recipes


app = Flask(__name__)
api = Api(app)

api.add_resource(MainMenu, "/")
api.add_resource(Recipes, "/recipes")


if __name__ == '__main__':
    app.run()
