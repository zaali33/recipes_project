from flask import Flask
from flask_restful import Api
from resources.main_menu import MainMenu


app = Flask(__name__)
api = Api(app)

api.add_resource(MainMenu, "/")


if __name__ == '__main__':
    app.run()
