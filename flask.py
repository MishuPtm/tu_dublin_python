from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

# App setup
engine = create_engine('sqlite:////database.db', echo=True)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# this command has to be ran after you make changes to models
# Make sure you delete old db file after any model changes
db.create_all()


@app.route('/')
def create_user():
    # just a test to see how to create data in database
    usr = User(username="joasdhn", email="asd@sdsd.com")
    db.session.add(usr)
    db.session.commit()
    return 'User created'


@app.route('/users')
def show_users():
    # just a test to see how to retrieve data from database
    users = User.query.all()
    response = {"users": []}
    for user in users:
        response["users"].append({"username": user.username,
                                  "email": user.email})
    return response


@app.route('/test_post', methods=['POST', 'GET'])
def test_post():
    # Just a test to see how to get json data.
    # use this request in gui, very important json keyword, if you use data or params it will not work:
    # result = requests.post("http://localhost:5000/test_post", json={"username": "asd", "email": "safoiuna"}})
    json_data = request.get_json()
    try:
        # keys in the dict should match properties for user
        usr = User(**json_data)
        db.session.add(usr)
        db.session.commit()
    except:
        return {"message": "Failed to create user"}
    return {"message": f"User {usr.id} created"}


if __name__ == '__main__':
    app.run()
