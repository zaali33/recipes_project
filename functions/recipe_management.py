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

    def import_recipes(self):
        f = request.files['file']
        imported_file = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], imported_file))
        new_file = open(UPLOAD_FOLDER + imported_file, 'r')
        old_file = open('data/recipes.json', 'w')
        old_file.write(new_file.read())

        new_file.close()
        old_file.close()
        load_recipes_from_file('data/recipes.json')

<<<<<<< HEAD
        return True
    
    def edit_recipe(self, recipe):
        recipe_from_file = None
        for rec in recipe_from_file:
            if rec.id == recipe.id:
                recipe_from_file = rec
                break
        if recipe_from_file is None:
            raiseExceptions("Recipe not found")
        recipe_from_file.id = recipe.id
        recipe_from_file.name = recipe.name
        recipe_from_file.description = recipe.description
        recipe_from_file.category = recipe.category
        recipe_from_file.rating = recipe.rating
        recipe_from_file.image_url = recipe.image_url
       
        # if not isinstance(employee.id, int):
        #     raise Exception("Id must be an integer")
    
        # if isinstance(employee.id, int) and employee.id <= 0:
        #     raise Exception("Id must be greater than 0")
        
        # if not isinstance(employee.name, str):
        #     raise Exception("Name must be a string")
    
        # if len(employee.name) == 0:
        #     raise Exception("Name must not be empty")

        # if not isinstance(employee.age, int):
        #     raise Exception("Age must be an integer")
    
        # if isinstance(employee.age, int) and employee.age <= 0:
        #     raise Exception("Age must be greater than 0")
        
        # if not isinstance(employee.department, str):
        #     raise Exception("Department must be a string")
    
        # if len(employee.department) == 0:
        #     raise Exception("Department must not be empty")
        
        # for emp in self.employees:
        #     if emp.id == employee.id:
        #         raise Exception("Duplicate Employee ID")
            
        # self.employees.append(employee)
=======
        os.remove(UPLOAD_FOLDER + imported_file)

        return True
>>>>>>> 87d0277cc35e4785d336d79bc7cfb8198669ccf2
