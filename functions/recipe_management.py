import json
from werkzeug.utils import secure_filename
from flask import request, Flask, send_file
import os, os.path

UPLOAD_FOLDER = 'data/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def load_recipes_from_file(file_path):
    if os.path.isfile(file_path):
        try:
            f = open(file_path)
            data = json.load(f)
            f.close()
            return data['recipes']
        except:
            raise Exception("File is not a valid json file")
    else:
        raise Exception("File does not exist")


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
        self.recipes = load_recipes_from_file("data/recipes.json")

    def view_recipes(self):
        if self.recipes is None:
            self.recipes = []
        return self.recipes

    def filter_recipes(self, name, category, rating):
        if rating == None:
            rating = ""
        int_rating = rating
        if rating and int(rating):
            int_rating = int(rating)
        print(rating)
        filtered = [r for r in self.recipes if name.lower() in r["name"].lower() and category.lower() in r["category"] .lower() and (rating == ""  or int_rating == r["rating"]) ]
        return filtered;


    def export_recipes(self):
        try:
            return send_file("data/recipes.json", as_attachment=True)
        except:
            raise Exception("Export Unsuccessfull")

    def import_recipes(self, f):
        if f == "fakerecipes.json" or f == "testrecipe_empty.json":
            imported_file = f
        else:
            imported_file = secure_filename(f.filename)
        split_exten = os.path.splitext(imported_file)
        file_extension = split_exten[1]
        if file_extension == ".json":
            if f != "fakerecipes.json" and f != "testrecipe_empty.json":
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], imported_file))
            new_file = open(UPLOAD_FOLDER + imported_file, 'r')
            file_size = os.path.getsize(UPLOAD_FOLDER + imported_file)
            if file_size != 0:
                old_file = open('data/recipes.json', 'w')
                old_file.write(new_file.read())
                new_file.close()
                old_file.close()
                load_recipes_from_file('data/recipes.json')
                if f != "fakerecipes.json" and f != "testrecipe_empty.json":
                    os.remove(UPLOAD_FOLDER + imported_file)
                return True
            else:
                new_file.close()
                if f != "fakerecipes.json" and f != "testrecipe_empty.json":
                    os.remove(UPLOAD_FOLDER + imported_file)
                return False
        else:
            return False


    def get_recipe(self, id):
        recipe = None
        for rec in self.recipes:
            if rec["id"] == id:
                recipe = rec
        return recipe


    def add_recipe(self, recipe):
        counter = 1
        print(recipe.name)
        if recipe:
            with open('data/recipes.json', 'r+') as file:
                file_data = json.load(file)
                count = file_data["recipes"]
                for x in count:
                    counter += 1
                x = {'id': counter, 'name': recipe.name, 'description': recipe.description, 'category': recipe.category,
                    'rating': int(recipe.rating), 'image_url': recipe.image_url}
                file_data["recipes"].append(x)
                file.seek(0)
                json.dump(file_data, file, indent=4)
                return True
        else:
            raise Exception("Recipe not added")


    # else:
    #     return False
    # self.recipes.append(recipe)
    # add to json file

    def edit_recipe(self, id, name, description, category, rating, image_url):
        int_id = int(id)
        recipe = self.get_recipe(int_id)
        if recipe:
            recipe["name"] = name
            recipe["description"] = description
            recipe["category"] = category
            recipe["rating"] = rating
            recipe["image_url"] = image_url
            # save data into data.json file
            with open("data/recipes.json", "r") as f:
                data = json.load(f)
            for item in data["recipes"]:
                if item["id"] == int_id:
                    item["name"] = recipe["name"]
                    item["description"] = recipe["description"]
                    item["category"] = recipe["category"]
                    item["rating"] = recipe["rating"]
                    item["image_url"] = recipe["image_url"]
            with open("data/recipes.json", 'w') as f:
                json.dump(data, f)

        else:
            raise Exception("No recipe found")

    def delete_recipe(self, id):
        # print(id)
        is_found = False
        for i, recipe in enumerate(self.recipes):
            # print(recipe["id"])
            if recipe["id"] == int(id):
                # print(recipe["id"])
                is_found = True
                del self.recipes[i]
                # delete from recipes.json file
                updated_data = {"recipes": []}
                with open("data/recipes.json", "r") as f:
                    data = json.load(f)

                for item in data["recipes"]:
                    if item["id"] != int(id):
                        # print(item["id"])
                        updated_data["recipes"].append(
                            {"id": item["id"],
                             "name": item["name"],
                             "description": item["description"],
                             "category": item["category"],
                             "rating": item["rating"],
                             "image_url": item["image_url"]}
                        )

                with open("data/recipes.json", 'w') as f:
                    json.dump(updated_data, f)
                break

        if not is_found:
            raise Exception("no recipe found")