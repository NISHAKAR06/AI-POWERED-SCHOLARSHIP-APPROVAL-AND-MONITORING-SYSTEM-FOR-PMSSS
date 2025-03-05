from flask import render_template, request, redirect, url_for, jsonify, flash, session
from . import app
from .forms import RegistrationForm, ApplicantForm, FamilyDetailsForm, BankDetailsForm, LoginForm
from pymongo import MongoClient
import random

# MongoDB Connection
client = MongoClient("mongodb+srv://ai_portal3:ai_portal3@cluster-aiportal.n80no.mongodb.net/")
db = client["Applicant_person_details"] 
users_collection = db["registrations"]
applicants_collection = db["applicants_details"]

@app.route('/status')
def status():
    return render_template('status.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user_id = random.randint(100000, 999999)  # Generate a unique 6-digit number
        
        if users_collection.find_one({"email": email}):
            return "Email already registered!"  # Handle duplicate email
        
        if users_collection.find_one({"username": username}):
            return "Username already taken!"  # Handle duplicate username
        
        while users_collection.find_one({"user_id": user_id}):  # Ensure unique ID
            user_id = random.randint(100000, 999999)
        
        users_collection.insert_one({"user_id": user_id, "name": name, "username": username, "email": email, "password": password})
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = users_collection.find_one({"email": email, "password": password})
        
        if user:
            session['email'] = email
            session['user_id'] = user['user_id']
            session['name'] = user['name']
            return redirect(url_for('home'))
        else:
            return "Invalid email or password!"
    return render_template('login.html')
# Ensure you have register.html in the templates folder

@app.route('/apply')
def apply_page():
    return render_template('apply.html')

@app.route('/')
def home():
    username = session.get('username')  # Get username from session
    return render_template('home.html', username=username)

@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('user_id', None)
    session.pop('name', None)
    return redirect(url_for('login'))

@app.route('/users')
def users():
    if 'email' not in session:
        return redirect(url_for('login'))
    user_data = list(users_collection.find({}, {"_id": 0, "user_id": 1, "name": 1, "email": 1}))
    return render_template('users.html', users=user_data)

@app.route('/apply', methods=['GET', 'POST'])
def apply_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        
        # Validate data
        if not data:
            return jsonify({'error': 'Invalid data'}), 400

        # Insert data into MongoDB
        applicants_collection.insert_one(data)
        return jsonify({'message': 'Application submitted successfully'}), 201
    
    return render_template('apply.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/applications', methods=['GET'])
def get_applications():
    applications = list(applicants_collection.find())
    return jsonify(applications), 200

if __name__ == '__main__':
    app.run(debug=True)