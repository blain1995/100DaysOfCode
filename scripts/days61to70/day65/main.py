from flask import Flask, render_template
import requests
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


@app.route('/contact')
def contact_details():
    return render_template('contact.html')


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for post in data:
        if post["id"] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
