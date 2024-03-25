from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, InputRequired, Length

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), InputRequired(), Length(min= 8)])
    submit = SubmitField(label='Log in')

app = Flask(__name__)
app.secret_key = "some secret string"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    LoginForm = MyForm()
    if LoginForm.validate_on_submit():
        if (LoginForm.email.data == "admin@email.com" and LoginForm.password.data == "12345678"):
            # @app.route("/success")
            # def success():
                return render_template('success.html')
        else :
            # @app.route("/denied")
            # def denied():
                return render_template('denied.html')
    return render_template('login.html', form=LoginForm)



if __name__ == '__main__':
    app.run(debug=True)
