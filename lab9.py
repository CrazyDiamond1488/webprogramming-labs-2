from flask import Blueprint, render_template, abort, redirect, request

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def main():
    return render_template('lab9/index.html')

@lab9.app_errorhandler(404)
def not_found(e):
    return render_template('lab9/404.html'), 404

@lab9.route('/lab9/500')
def trigger_500_error():
    return render_template('lab9/500.html'), 500

@lab9.route('/lab9/happy', methods=['GET'])
def greeting_card():
    name = request.args.get('name', '')
    gender = request.args.get('gender', '')
    sender_name = request.args.get('sender_name', '')
    greeting = ''

    if name and gender and sender_name:
        greeting = create_greeting(name, gender, sender_name)

    return render_template('lab9/happy.html', name=name, gender=gender, sender_name=sender_name, greeting=greeting)

def create_greeting(name, gender, sender_name):
    if gender == 'мужской':
        greeting = f'Дорогой {name},\n\n'
    else:
        greeting = f'Дорогая {name},\n\n'
    greeting += f'С Новым годом! Желаю счастья, здоровья и успехов в новом году.\n\n'
    greeting += f'С наилучшими пожеланиями,\n{sender_name}'
    return greeting

