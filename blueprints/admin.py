from flask import Blueprint ,redirect,abort,render_template,session ,request
import config


app = Blueprint("admin" , __name__)

@app.before_request
def before_request():
    if session.get('admin_login' , None) == None and request.endpoint != "admin_login":
        abort(403)


@app.route('/admin' , methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username" , None)
        password = request.form.get("password",None)

        if username == config.ADMIN_USERNAME and password == config.ADMIN_PASSWORD:
            session ['admin_login'] = username
            return redirect("admin/dashboard")
        else:
            return redirect("admin")
        
    else:
        return render_template("admin/login.html")
