from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log in')

app = Flask(__name__)
app.secret_key = "some secret string"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    LoginForm = MyForm()
    return render_template('login.html', form=LoginForm)



if __name__ == '__main__':
    app.run(debug=True)
