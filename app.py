from flask import Flask, render_template, request, flash, redirect, url_for
from pymongo import MongoClient
from config import MONGODB_CONFIG
from urllib.parse import quote_plus

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for using flash messages

# Properly escape the username and password for MongoDB URI
username = quote_plus(MONGODB_CONFIG['username'])
password = quote_plus(MONGODB_CONFIG['password'])
cluster_url = MONGODB_CONFIG['cluster_url']
database_name = MONGODB_CONFIG['database']

# Create the MongoDB client
client = MongoClient(f"mongodb+srv://{username}:{password}@{cluster_url}/{database_name}?retryWrites=true&w=majority")
db = client[database_name]
cars_collection = db['cars']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        if name and email and subject and message:
            flash('Thank you for your message! We will get back to you soon.', 'success')
            return redirect(url_for('contact'))
        else:
            flash('Please fill in all fields.', 'error')
            
    return render_template('contact.html')

@app.route('/car_details', methods=['POST'])
def car_details():
    brand = request.form.get('brand')
    model = request.form.get('model')
    year = request.form.get('year')
    
    if brand and model and year:
        car = cars_collection.find_one({
            'Brand': brand,
            'Model': model,
            'Year': int(year)
        })
        
        if car:
            return render_template('car_details.html', car=car)
        else:
             return render_template('car_details.html', message='No car found with the provided details.')
    else:
        flash('Please fill in all fields for the search.', 'error')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
