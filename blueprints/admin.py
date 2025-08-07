from flask import Blueprint,flash ,redirect,abort,render_template,session ,request
import config

from models.cart import Cart

app = Blueprint("admin" , __name__)

@app.before_request
def before_request():
    if session.get('admin_login' , None) == None and request.endpoint != "admin.admin_login":
        abort(403)


@app.route('/admin' , methods=["POST", "GET"])
def admin_login():
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


@app.route('/admin/dashboard' , methods = ["GET"])
def dashboard_admin():
    carts = Cart.query.filter(Cart.status != 'pending').all()
    return render_template("admin/dashboard.html" , carts = carts)


@app.route('/admin/logout', methods = ['GET'])
def logout():
    session.pop('admin_login',None)
    flash('با موفقیت خارج شدید')
    return redirect('/admin')