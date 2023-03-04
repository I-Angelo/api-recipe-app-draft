from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Recipe, recipe_schema, recipes_schema 

api = Blueprint('api', __name__, url_prefix = '/api')


@api.route('/myrecipes', methods = ['POST'])
@token_required
def create_recipe(current_user_token):
    name = request.json['name'] 
    ingredient = request.json['ingredient']
    process = request.json['process']
    # image_file = request.files['image']
    # image = image_file.read()
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    recipe = Recipe(name=name, ingredient=ingredient, process=process, user_token = user_token) 

    db.session.add(recipe) 
    db.session.commit() 

    response = recipe_schema.dump(recipe)
    return jsonify(response)

@api.route('/myrecipes', methods = ['GET'])
@token_required
def get_recipe(current_user_token):
    a_user = current_user_token.token
    recipes = Recipe.query.filter_by(user_token = a_user).all()
    response = recipes_schema.dump(recipes)
    return jsonify(response)    



@api.route('/myrecipes/<id>', methods = ['GET'])
@token_required
def get_single_recipe(current_user_token, id):
    # a_user = current_user_token.token
    recipe = Recipe.query.get(id)
    response = recipe_schema.dump(recipe)
    return jsonify(response)


@api.route('/myrecipes/<id>', methods = ['POST', 'PUT'])
@token_required
def update_recipe(current_user_token, id): 
    recipe = Recipe.query.get(id)
    recipe.name = request.json['name']
    recipe.ingredient = request.json['ingredient']
    recipe.process = request.json['process']
    # recipe.image = request.json['image']
    recipe.user_token = current_user_token.token

    db.session.commit()
    response = recipe_schema.dump(recipe)
    return jsonify(response)


@api.route('/myrecipes/<id>', methods = ['DELETE'])
@token_required
def delete_recipe(current_user_token, id):
    # a_user = current_user_token.token
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    response = recipe_schema.dump(recipe)
    return jsonify(response)




