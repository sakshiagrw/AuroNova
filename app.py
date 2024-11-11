from flask import Flask, render_template,request, jsonify
app = Flask(__name__)

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

# @app.route('/services')
# def services():
#     return render_template('services.html')

if __name__ == '__main__':
    app.run(debug=True)