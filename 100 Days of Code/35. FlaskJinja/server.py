from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/guess/<name>")
def get_guess(name):
    # random_number = random.randint(1,10)
    # tahun = datetime.datetime.now().year
    responsegender = requests.get(f"https://api.genderize.io/?name={name}")
    responseage = requests.get(f"https://api.agify.io/?name={name}")
    genderdict = responsegender.json()
    agedict = responseage.json()
    return render_template("index.html", gender = genderdict['gender'], age = agedict['age'], name=name.capitalize())

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts =all_posts)

if __name__ == "__main__":
    app.run(debug=True)



