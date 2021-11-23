from app import app
from flask import render_template
from flask import request
from validators.signupform import SignUpFromValidator


@app.route('/login')
def login():
    
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register_user', methods=['POST'])
def register():
    print(request.form)
    form = SignUpFromValidator(request.form)
    if request.method == 'POST' and form.validate():
        return 'Life is great you know'
    return render_template('signup.html', form=form)
    
@app.route('/logout')
def logout():
    return 'Logout'