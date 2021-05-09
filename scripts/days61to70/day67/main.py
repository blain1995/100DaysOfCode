from flask import Flask, render_template, request
from smtplib import SMTP
import os
import requests

my_email = os.environ.get("MY_EMAIL")
my_pass = os.environ.get("EMAIL_PASS")

app = Flask(__name__)
api_endpoint = 'https://api.npoint.io/0067e63917ca7a5034d9'

response = requests.get(url=api_endpoint)
data = response.json()


@app.route('/')
def hello_world():
    return render_template('index.html', blog_posts=data)


@app.route('/about')
def about_me():
    return render_template('about.html')


@app.route('/contact', methods=["GET", "POST"])
def contact_details():
    if request.method == "POST":
        user_data = request.form
        name = user_data['name']
        email = user_data['email']
        phone = user_data['phone']
        message = user_data['message']
        connection = SMTP(host='smtp.gmail.com', port=587)
        connection.starttls()
        connection.login(my_email, my_pass)
        connection.sendmail(msg=f"New Message from {name}\n\n{message}\nPhone: {phone}\nEmail: {email}",
                                from_addr=my_email, to_addrs=my_email)
        return render_template('contact.html', sent_msg=True)
    return render_template('contact.html', sent_msg=False)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for post in data:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
