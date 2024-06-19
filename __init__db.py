from app import app, db
from app.models import Post


def create_table():
    p1 = Post(title="Post 1", content="some content for post 1", user="anonimus")
    p2 = Post(title="Post 2", content="some content for post 2", user="anonimus")
    p3 = Post(title="Post 3", content="some content for post 3", user="anonimus")


    db.session.add_all([p1, p2, p3])
    db.session.commit()
    print("Data created")




with app.app_context():
    # db.create_all()
    print("Create db")
    create_table()