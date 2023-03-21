from flask_restful import Resource
from flask import Response, render_template, redirect
from functions.recipe_management import RecipeManagement
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, HiddenField
from wtforms.validators import DataRequired, NumberRange

class RecipeForm(FlaskForm):
    id = HiddenField()
    name = StringField(label="Name", validators=[DataRequired()])
    description = TextAreaField(label="Description", validators=[DataRequired()])
    image_url = StringField(label="Image URL", validators=[DataRequired()])
    category = StringField(label="Category", validators=[DataRequired()])
    rating = IntegerField(label="Rating", validators=[NumberRange(1, 5)])

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

class RecipesEdit(Resource):
    def get(self, id):
        recipe_management = RecipeManagement()
        recipe = recipe_management.get_recipe(id)
        recipe_form = RecipeForm()
        if recipe:
            recipe_form.id.data = recipe["id"]
            recipe_form.name.data = recipe["name"]
            recipe_form.description.data = recipe["description"]
            recipe_form.image_url.data = recipe["image_url"]
            recipe_form.category.data = recipe["category"]
            recipe_form.rating.data = recipe["rating"]
        return Response(response=render_template("edit_recipe.html", recipe=recipe, recipe_form=recipe_form))

    def post(self):
        recipe_form = RecipeForm()
        recipe_management = RecipeManagement()
        if recipe_form.validate_on_submit():
            recipe_management.edit_recipe(int(recipe_form.data.get('id')), recipe_form.data.get("name"),
                                          recipe_form.data.get("description"), recipe_form.data.get("category"),
                                          recipe_form.data.get("rating"), recipe_form.data.get("image_url"))
            return redirect("/recipes")
        else:
            recipe = recipe_management.get_recipe(recipe_form.data.get('id'))
            return Response(response=render_template('edit_recipe.html', recipe=recipe, recipe_form=recipe_form))