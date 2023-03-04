# helps us with our data bases so they are created on our behalf on the databases sites
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate  
import uuid 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow 
import secrets


login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)  
    first_name = db.Column(db.String(150), nullable=True, default='') 
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False) 
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True )
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow) 


    def __init__(self, email, first_name, last_name, password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length): 
        return secrets.token_hex(length)    

    def set_id(self):
         return str(uuid.uuid4())

    def set_password(self, password): 
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash 

    def __repr__(self): 
        return f'User {self.email} has been added to the database'



class UserSchema(ma.Schema):
    class Meta:
        fields = ['id', 'last_name', 'email', 'first_name']


user_schema = UserSchema()
users_schema = UserSchema(many = True)



# class Register(db.Model):
#     id = db.Column(db.String, primary_key=True)  
#     email = db.Column(db.String(150), nullable = False) 
#     first_name = db.Column(db.String(150), nullable=True, default='') 
#     last_name = db.Column(db.String(150), nullable = True, default = '')
#     password = db.Column(db.String, nullable = True, default = '')
#     # g_auth_verify = db.Column(db.Boolean, default = False)
#     token = db.Column(db.String, default = '', unique = True )
#     date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow) 
#     # user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

#     def __init__(self, email, first_name='', last_name='', password='', id=''): # token='', g_auth_verify=False
#         self.id = self.set_id()
#         self.email = email
#         self.first_name = first_name
#         self.last_name = last_name
#         self.password = self.set_password(password)
#         self.token = self.set_token(24)
#         # self.g_auth_verify = g_auth_verify

#     def set_token(self, length): 
#         return secrets.token_hex(length)    

#     def set_id(self):
#          return str(uuid.uuid4())

#     def set_password(self, password): 
#         self.pw_hash = generate_password_hash(password)
#         return self.pw_hash 

#     def __repr__(self): 
#         return f'User {self.email} has been registered to the database'


# class RegisterSchema(ma.Schema):
#     class Meta:
#         fields = ['id', 'email', 'first_name', 'last_name', 'password']


# register_schema = RegisterSchema()
# registers_schema = RegisterSchema(many = True)


class Recipe(db.Model):
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String(200), nullable = False, default='')
    ingredient = db.Column(db.String(700), nullable = False, default='')
    process = db.Column(db.String(2000), nullable = False, default='')
    # image = db.Column(db.LargeBinary(10000), nullable = False)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, name, ingredient, process, user_token, id=''):
        self.id = self.set_id()
        self.name = name
        self.ingredient = ingredient
        self.process = process
        # self.image = image
        self.user_token = user_token

    def __repr__(self):
        return f'The following poison has been created : {self.name}'

    def set_id(self):
        return (secrets.token_urlsafe())


class RecipeSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'ingredient', 'process']


recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many = True)

