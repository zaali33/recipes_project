import json
from werkzeug.utils import secure_filename
from flask import request, Flask
import os, os.path

UPLOAD_FOLDER = 'data/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def load_recipes_from_file(file_path):
    f = open(file_path)
    data = json.load(f)
    f.close()
    return data['recipes']


class Recipe:
    def __init__(self, id, name, description, category, rating, image_url):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.rating = rating
        self.image_url = image_url


class RecipeManagement:
    def __init__(self):
        self.recipes = load_recipes_from_file('data/recipes.json')

    def view_recipes(self):
        if self.recipes is None:
            self.recipes = []
        return self.recipes


    def export_recipes(self):
        with open('data/recipes.json', 'r') as file:
            save_file = json.load(file)
            save_file.close()
        return save_file
        #file = load_recipes_from_file('data/recipes.json')
        #if os.path.exists(file):
            #with open(file, 'r') as f:
                #save_file = json.load(f)
                #save_file.close()
            #return file

    def import_recipes(self):
        f = request.files['file']
        imported_file = secure_filename(f.filename)
        split_exten = os.path.splitext(imported_file)
        file_extension = split_exten[1]
        # print("File Extension: ", file_extension)
        if file_extension == ".json":
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], imported_file))
            new_file = open(UPLOAD_FOLDER + imported_file, 'r')
            old_file = open('data/recipes.json', 'w')
            old_file.write(new_file.read())

            new_file.close()
            old_file.close()
            load_recipes_from_file('data/recipes.json')

            os.remove(UPLOAD_FOLDER + imported_file)
            return True
        else:
            return False
