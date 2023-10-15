from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    user = request.args.get('user')
    age = request.args.get('age')
    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex)