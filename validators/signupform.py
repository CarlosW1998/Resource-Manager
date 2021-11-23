from wtforms import Form, EmailField,StringField, PasswordField, validators

class SignUpFromValidator(Form):
    username = StringField('username', 
        [validators.Length(min=3, max=150), validators.DataRequired()])
    password = PasswordField('password', 
        [validators.DataRequired(), validators.Length(min=8, max=50)])
    email = EmailField('email',
        [validators.DataRequired(), validators.Email()])