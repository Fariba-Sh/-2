from flask import Blueprint,render_template

app = Blueprint("user" , __name__)

@app.route('/user/login')
def login():
    return render_template("user/login.html")