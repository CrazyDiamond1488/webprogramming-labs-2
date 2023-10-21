from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method =='GET':
        return render_template("login.html")

    username = request.form.get('username')
    password = request.form.get('password')
    error = None 
    if not username and not password:
        error = 'Нет логина и пароля'
    elif not username:
        error = 'Нет логина'
    elif not password:
        error = 'Нет пароля'
    elif username == 'Crazydiamond' and password == 'Asustufgaming':
        return render_template("succes4.html", username=username)
    else:
        error = 'Неверный логин или пароль!'

    return render_template("login.html", error=error, username=username, password=password)


@lab4.route('/lab4/freeze', methods=['GET', 'POST'])
def freeze():
    if request.method == 'GET':
        return render_template("freeze.html")
    
    temperature = request.form.get('temperature')
    if  not temperature:
        result = 'ошибка: не задана температура!'
    elif int(temperature) <= -12:
        result = 'не удалось установить температуру — слишком низкое значение'
    elif int(temperature) > -1:
        result = 'не удалось установить температуру — слишком высокое значение'
    elif int(temperature) > -12 and int(temperature) < -9:
        result = f"Установлена температура: {temperature}°C ***"
    elif int(temperature) >= -8 and int(temperature) <= -5:
        result = f"Установлена температура: {temperature}°C **"
    elif int(temperature) >= -4 and int(temperature) <= -1:
        result = f"Установлена температура: {temperature}°C *"

    return render_template("freeze.html", result=result)

@lab4.route('/lab4/zerno',  methods=['GET', 'POST'])
def zerno():
    if request.method == 'GET':
        return render_template("zerno.html")
    
    zerno = request.form.get('zerno')
    weight = int(request.form.get('weight'))
    price = 0
    
    if zerno == 'ячмень':
        price = 12000
    elif zerno == 'овёс':
        price = 8500
    elif zerno == 'пшеница':
        price = 8700
    elif zerno == 'рожь':
        price = 14000
    
    if weight <= 0:
        errors = 'Не верно указан объём закупки'
        return render_template("zerno.html", errors=errors)
    elif weight >= 500:
        errors = 'Извините, но такого количества зерна, пока что нет в наличии'
        return render_template("zerno.html", errors=errors)
    
    if weight > 50:
        total_price = (weight * price) * 0.9
        message = f"Заказ успешно сформирован. Вы заказали {zerno}. Вес: {weight} т. " \
                  f"Сумма к оплате: {total_price} руб. (Применена скидка за большой объем)"
    else:
        total_price = weight * price
        message = f"Заказ успешно сформирован. Вы заказали {zerno}. Вес: {weight} т. " \
                  f"Сумма к оплате: {total_price} руб."
        
    return render_template('zerno.html', message=message)
    

