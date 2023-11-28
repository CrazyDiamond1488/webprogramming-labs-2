from flask import Blueprint, redirect, url_for, render_template, request, session
from Db import db

from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user

lab6 = Blueprint('lab6', __name__)

@lab6.route('/lab6/')
def lab():
    return render_template('lab6.html')

@lab6.route('/lab6/check')
def main():
    my_users = users.query.all()
    print(my_users)
    return "result it console!"


@lab6.route("/lab6/checkarticles")
def checkarticles():
    my_acticles = articles.query.all()
    print(my_acticles)
    return "result it console!"

@lab6.route('/lab6/glav')
def lab6_glav():
    username_form = session.get('username')
    return render_template('glav6.html', username = username_form)


@lab6.route('/lab6/register', methods = ['GET', 'POST'])
def register():
    errors = []
    if request.method == 'GET':
        return render_template('register6.html')
    
    username_form = request.form.get('username')
    password_form = request.form.get('password')

    isUserExist = users.query.filter_by(username=username_form).first()
    if isUserExist is not None:
        errors.append("Пользователь уже существует")
        return render_template('register6.html', errors=errors)   

    if not (username_form or password_form):
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('register6.html', errors=errors)
    if username_form == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('register6.html', errors=errors)
    if password_form == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('register6.html', errors=errors)
    
    if len(password_form) < 5:
            errors.append("Пароль должен содержать не менее 5 символов")
        
    
    hashPassword = generate_password_hash(password_form, method='pbkdf2')
    newUser = users(username=username_form, password=hashPassword)

    db.session.add(newUser)
    db.session.commit()

    return redirect('/lab6/login')

@lab6.route('/lab6/login', methods=["GET", "POST"])
def login6():
    errors = []
    if request.method == "GET":
        return render_template("login6.html")
    
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    if not (username_form and password_form):
            errors.append("Пожалуйста, заполните все поля")

    my_user = users.query.filter_by(username=username_form).first()
    if my_user is not None:
        
        if check_password_hash(my_user.password, password_form):
            login_user(my_user, remember=False)
            return redirect("/lab6/glav")
        
    return render_template("login6.html")


@lab6.route("/lab6/articles")
def articles_list():
    my_articles = articles.query.filter_by(user_id=current_user.id).all()
    return render_template("articles6.html", articles=my_articles)


@lab6.route("/lab6/newarticle", methods=["GET", "POST"])
@login_required
def createArticle():
    if request.method == "GET":
        return render_template("newarticle6.html")

    article_text = request.form.get("article_text")
    title = request.form.get("article_title")

    if len(article_text) == 0:
        errors = ["Заполните текст"]
        return render_template("newarticle6.html", errors=errors)

    new_article = articles(user_id=current_user.id, title=title, article_text=article_text)
        

    db.session.add(new_article)
    db.session.commit()
    
    return redirect("/lab6/articles")

@lab6.route("/lab6/articles/<int:article_id>")
@login_required
def viewArticle(article_id):
    article = articles.query.filter_by(id=article_id).first()
    if article:
        return render_template("articles6.html", article=article)
    

   


