from flask_mongoengine import MongoEngine

db = MongoEngine()  # Initialize MongoDB

class Registration(db.Document):
    username = db.StringField(required=True)
    email = db.EmailField(required=True)

class Applicant(db.Document):  # Ensure this class exists
    name = db.StringField(required=True)
    email = db.EmailField(required=True)

class FamilyDetails(db.Document):
    father_name = db.StringField(required=True)
from flask_mongoengine import MongoEngine

db = MongoEngine()  # Initialize MongoDB

class User(db.Document):
    username = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    phone = db.StringField(required=True, unique=True)  # Allows international formats
    dob = db.DateTimeField(required=True)
    password_hash = db.StringField(required=True)

class Registration(db.Document):
    username = db.StringField(required=True)
    email = db.EmailField(required=True)
    phone = db.StringField(required=True)  # Updated to allow international formats
    dob = db.DateTimeField(required=True)
    password_hash = db.StringField(required=True)

class Applicant(db.Document):  
    name = db.StringField(required=True)
    email = db.EmailField(required=True)
    phone = db.StringField(required=True)  # Updated to allow international formats

class FamilyDetails(db.Document):
    father_name = db.StringField(required=True)
    mother_name = db.StringField(required=True)
    guardian_name = db.StringField()  # Made optional

class BankDetails(db.Document):
    account_number = db.StringField(required=True, unique=True)
    ifsc_code = db.StringField(required=True)
    bank_name = db.StringField(required=True)
    branch_name = db.StringField(required=True)  # Added branch name field

class BankDetails(db.Document):
    account_number = db.StringField(required=True)
