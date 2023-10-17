from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    return render_template("lab3.html")


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template("form1.html", user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else: 
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('pay.html', price=price)

@lab3.route('/lab3/succes')
def succes():
    return render_template('succes.html')


@lab3.route('/lab3/tiket')
def tiketpay():
    return render_template('tiket.html')

@lab3.route('/lab3/tiketpay')
def tiket():
    pricetiket = 0
    tiket = request.args.get('tiket')
    if tiket == 'детский':
        pricetiket = 1000
    else:
        pricetiket = 1800

    if request.args.get('baggage') == 'on':
        pricetiket += 600
    return render_template('tiketpay.html', pricetiket=pricetiket)


@lab3.route('/lab3/succestiket')
def succestiket():
    return render_template('succestiket.html')