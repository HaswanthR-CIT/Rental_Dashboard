from flask import Flask, render_template, request

app = Flask(__name__)

# Hardcoded valid login (for simplicity)
VALID_EMAIL = "test@example.com"
VALID_PASSWORD = "password123"

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if email == VALID_EMAIL and password == VALID_PASSWORD:
        return render_template('dashboard.html')
    else:
        return render_template('login.html', error="Invalid email or password!")

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/search_property')
def search_property():
    return render_template('search_property.html')

@app.route('/compare_property')
def compare_property():
    return render_template('compare_property.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/admin_info')
def admin_info():
    return render_template('admin_info.html')

if __name__ == '__main__':
    app.run(debug=True)