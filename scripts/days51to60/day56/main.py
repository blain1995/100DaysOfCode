from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

all_posts = requests.get(url=" https://api.npoint.io/5abcca6f4e39b4955965").json()
post_list = []
for post in all_posts:
    post_features = Post(post['id'], post['title'], post['subtitle'], post['body'])
    post_list.append(post_features)


@app.route('/')
def home():
    return render_template("index.html", blogs=post_list)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_list:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
