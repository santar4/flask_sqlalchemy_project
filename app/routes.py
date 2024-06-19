from flask import render_template
from app import app, db
from app.models import Post


@app.route("/")
def home():
    stmt = db.select(Post)
    posts = db.session.execute(stmt).scalars()


    return render_template("home.html", posts=posts)

@app.route("/post/<int:post_id>/")
def post_detail(post_id):
    post = db.get_or_404(Post, post_id)
    print(post)
    return render_template("Posts/post.html", post=post)