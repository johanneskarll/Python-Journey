from flask import Flask, render_template, request
import requests
from post import Post
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

my_gmail = os.getenv("MYGMAIL")
password = os.getenv("EMAIL50PASS")

response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
app = Flask(__name__)

post_objects = []
for post in response:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

@app.route("/")
def home():
    return render_template("index.html", post=response)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        data = request.form
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_gmail, password=password)
            connection.sendmail(
                from_addr=my_gmail,
                to_addrs="johanneskarl50@gmail.com", 
                msg=f"Name: {data["name"]}\nEmail: {data["email"]}\nPhone: {data["phone"]}\nMessage: {data["message"]}"
            )
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__== "__main__":
    app.run(debug=True)