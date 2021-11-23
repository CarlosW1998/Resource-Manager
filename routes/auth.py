from app import app
from flask import render_template
from flask import request
from validators.signupform import SignUpFromValidator
from models.model import User
from hashlib import sha256

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register_user', methods=['POST'])
def register():
    form = SignUpFromValidator(request.form)
    if request.method == 'POST' and form.validate():
        with app.session() as session:
            user = User(name=form.username.data, email=form.email.data,
             password=sha256(form.password.data.encode('utf8')).hexdigest(), role="user")
            session.add(user)
            session.commit()
        return 'Life is great you know'
    return render_template('signup.html', form=form)
    
@app.route('/logout')
def logout():
    return 'Logout'