from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import migrate,Migrate
import os
#creting flask object (my application)
app=Flask(__name__)
#depug status is on
app.debug=True
#run app
#creating content:
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///antiquity.db'
app.config['UPLOAD_FOLDER']='static/uploads/'
# app.config['SECRET_KEY']='mysecret'
app.config['MAX_CONTENT']=16*1024*1024
ALLOWED_EXTENSIONS=['jpg','jpeg','png','gif']
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
db=SQLAlchemy(app)
#creating sites class
class Sites(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    site_name=db.Column(db.String(20), unique=False, nullable=False)
    about=db.Column(db.String, unique=False, nullable=False)
    waze_at=db.Column(db.String(20), unique=True, nullable=False)
    filename=db.Column(db.String(100), unique=False, nullable=True)

    def __repr__(self):
        return f"Name: {self.site_name}, Location: {self.waze_at}"
#creating users class
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique=False, nullable=False)
    user_email = db.Column(db.String(20), unique=False, nullable=False)
    user_password = db.Column(db.String(20), unique=False, nullable=False)
    def __repr__(self):
        return f"Name: {self.user_name}"
#creating reviews class
class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.Integer, unique=False, nullable=False)
    user_name = db.Column(db.String(20), unique=False, nullable=False)
    review_text = db.Column(db.String, unique=False, nullable=False)
    def __repr__(self):
        return f"Name: {self.name}, Content: {self.review_text}"
with app.app_context():
    db.create_all()
#migrate the data base to the application
migrate = Migrate(app, db)
#managment of the app:
@app.route("/")
def main_page():
    sites_info = Sites.query.all()
    return render_template("main_page.html", sites_info=sites_info)
#--------------------------site management----------------------------------#
@app.route("/add_sitee")
def add_sitee():
    return render_template("add_site.html")

@app.route("/add_site", methods=["POST","GET"])
def new_site():
    if request.method=="POST":
        site_name=request.form.get("site_name")
        about=request.form.get("about")
        waze_at=request.form.get("waze_at")
        file=request.files.get("filename")
        if allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        file_name = file.filename
        site_row=Sites(site_name=site_name,about=about,waze_at=waze_at,filename=file_name)
        db.session.add(site_row)
        db.session.commit()
        return redirect("/")
#---------------------------user management---------------------------------#
@app.route("/log_in")
def log_in():
    return render_template("log_in.html")

@app.route("/add_userr")
def add_userr():
    return render_template("sign_up.html")

@app.route("/add_user", methods=["POST","GET"])
def new_user():
    if request.method=="POST":
        user_name=request.form.get("user_name")
        user_email=request.form.get("user_email")
        user_password=request.form.get("user_password")
        user_row=Users(user_name=user_name,user_email=user_email,user_password=user_password)
        db.session.add(user_row)
        db.session.commit()
        return redirect("/")

#---------------------------reviews management------------------------------#
@app.route("/add_review/<int:id>",methods=["POST","GET"])
def new_review(id):
    if request.method=="POST":
        user_name=request.form.get("user_name")
        review_text=request.form.get("user_comment")
        site_id=request.form.get("site_id")
        review_row=Reviews(user_name=user_name,review_text=review_text,site_id=site_id)
        db.session.add(review_row)
        db.session.commit()
        return redirect(url_for('site_info', site_id=id))
    else:
        return render_template("site_info.html")

#---------------------------show site-----------------------------------------#
@app.route("/display/<filename>")
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename))

@app.route('/show_site/<int:site_id>')
def site_info(site_id):
    sites_specific = Sites.query.get(site_id)
    reviews_specific = Reviews.query.filter(Reviews.site_id == site_id)
    return render_template("show_site.html",sites_specific=sites_specific,reviews_specific=reviews_specific) #reviews_specific=reviews_specific)

@app.route("/delete/<int:id>")
def erase(id):
    data = Sites.query.get(id)
    filename = data.filename
    os.remove(f"{app.config['UPLOAD_FOLDER']}/{filename}")
    db.session.delete(data)
    reviews_specific = Reviews.query.filter(Reviews.site_id == id)
    for review in reviews_specific:
        db.session.delete(review)
    db.session.commit()
    return redirect("/")

@app.route("/alter_site/<int:id>", methods=["POST", "GET"])
def alter_site(id):
    if request.method == "POST":
        data = Sites.query.get(id)
        site_name = request.form.get("site_name")
        about = request.form.get("about")
        waze_at = request.form.get("waze_at")
        file = request.files.get("filename")
        if allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        file_name = file.filename
        if request.form.get("site_name"):
            data.site_name = site_name
        if request.form.get("about"):
            data.about = about
        if request.form.get("waze_at"):
            data.waze_at = waze_at
        if request.files.get("filename"):
            data.filename = file_name
        db.session.commit()
        return redirect(url_for('site_info', site_id=id))
    else:
        return render_template("update_site.html")
#!!
if __name__=="__main__":
    app.run()