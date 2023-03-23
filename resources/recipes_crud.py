from flask_restful import Resource
from flask import Response, render_template, redirect, request
from functions.recipe_management import RecipeManagement, Recipe
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, HiddenField
from wtforms.validators import DataRequired, NumberRange, InputRequired, Optional


class RecipeForm(FlaskForm):
    id = HiddenField()
    name = StringField(label="Name", validators=[DataRequired()])
    description = TextAreaField(label="Description", validators=[DataRequired()])
    image_url = StringField(label="Image URL", validators=[DataRequired()])
    category = StringField(label="Category", validators=[DataRequired()])
    rating = IntegerField(label="Rating", validators=[NumberRange(1, 5)])

class RecipeSearchForm(FlaskForm):
    name = StringField(label="Name")
    category = StringField(label="Category")
    rating = IntegerField(label="Rating", validators=[Optional()])

# view (get) and add (post) functions will be called in this class
class Recipes(Resource):
    def get(self):
        recipe_management = RecipeManagement()
        recipes = recipe_management.view_recipes()
        recipe_search_form = RecipeSearchForm()
        return Response(response=render_template("view.html", recipes=recipes, recipe_search_form=recipe_search_form))
    
    def post(self):
        recipe_search_form = RecipeSearchForm()
        if recipe_search_form.validate_on_submit():
            recipe_management = RecipeManagement()
            filtered_recipes = recipe_management.filter_recipes(
                recipe_search_form.data.get("name"), recipe_search_form.data.get("category"), recipe_search_form.data.get("rating")
            )
            return Response(response=render_template("view.html", recipes=filtered_recipes, recipe_search_form=recipe_search_form))
        else:
            return Response(response=render_template('view.html', recipe_search_form=recipe_search_form))

class Recipes_export(Resource):
    def get(self):
        recipe_management = RecipeManagement()
        return recipe_management.export_recipes()
    
class RecipeAdd(Resource):
    def get(self):
        recipe_form = RecipeForm()
        return Response(response=render_template("add-recipe.html", recipe_form=recipe_form))
    
    def post(self):
        # recipe = Recipe(id,name=request.form['recipeName'],
        #                 #   ingredients=request.form['recipeIngredients'],
        #                   description=request.form['recipeInstructions'],
        #                   category=request.form['recipeCategory'],
        #                   rating=request.form['recipeRating'],
        #                   image_url=request.form['recipeImage'])

        # recipe_management = RecipeManagement()
        # result = recipe_management.add_recipe(recipe)
        # return Response(response=render_template("added-success.html", result = result))
    
        recipe_form = RecipeForm()
        recipe_management = RecipeManagement()
        if recipe_form.validate_on_submit():
            recipe = Recipe(  
            id,name=recipe_form.data.get("name"),
        #   ingredients=request.form['recipeIngredients'],
            description=recipe_form.data.get("description"),
            category=recipe_form.data.get("category"),
            rating=recipe_form.data.get("rating"),
            image_url=recipe_form.data.get("image_url"))          
            recipe_management.add_recipe(recipe)
            return redirect("/recipes")
        else:
            # recipe = recipe_management.get_recipe(recipe_form.data.get('id'))
            return Response(response=render_template('add-recipe.html', recipe_form=recipe_form))

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

class RecipesImport(Resource):
    def get(self):
        return Response(response=render_template("import-recipes.html"))

    def post(self):
        recipe_management = RecipeManagement()
        result = recipe_management.import_recipes()
        return Response(response=render_template("import-success.html", result=result))


class RecipeDelete(Resource):
    def get(self):
        recipe_management = RecipeManagement()
        id = request.args.get("id")
        try:
            recipe_management.delete_recipe(id)
        except:
            return redirect("/recipes")
        return redirect("/recipes")
