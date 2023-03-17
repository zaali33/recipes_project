from flask_restful import Resource
from flask import Response, render_template


class MainMenu(Resource):
    def get(self):
        return Response(response=render_template("main-menu.html"))

