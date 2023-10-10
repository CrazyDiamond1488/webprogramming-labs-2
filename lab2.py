from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/example/')
def example():
    name = "Юстиниан Шишки"
    group = "ФБИ-14"
    curs = "3 курс"
    lab = "Лабораторная работа 2"
    fruits = [
        {'name': 'яблоки', 'price':100},
        {'name': 'грущи', 'price':120},
        {'name': 'апельсины', 'price':80},
        {'name': 'мандарины', 'price':95},
        {'name': 'манго', 'price':321}
    ]
    
    book = [
        {'avtor': 'Дэниел Киз ', 'name': 'Цветы для Элджернона', 'jshanr': 'Роман', 'str':320},
        {'avtor': 'Марк Саммерфилд ', 'name': 'Python 3. Профессиональное программирование', 'jshanr': 'Программирование', 'str':1024},
        {'avtor': 'Джоэл Грас', 'name': 'Fluent Python', 'jshanr': 'Программирование', 'str':792},
        {'avtor': 'Эрик Мэтиз ', 'name': 'Изучаем Python', 'jshanr': 'Программирование', 'str':624},
        {'avtor': 'Альберт Свергайт', 'name': 'Автоматизация рутины с помощью Python', 'jshanr': 'Программирование', 'str':592},
        {'avtor': 'Марк Лутц', 'name': 'Изучаем Python', 'jshanr': 'Программирование', 'str':1616},
        {'avtor': 'Дэн Бедер', 'name': 'Python для сложных задач', 'jshanr': 'Программирование', 'str':672},
        {'avtor': 'Дэвид Бизли', 'name': 'Python. Тестирование, web-разработка, наука и изучение данных', 'jshanr': 'Программирование', 'str':512},
        {'avtor': 'Аллен Б. Дауни', 'name': 'Learn Python Hard Way', 'jshanr': 'Программирование', 'str':385},
        {'avtor': 'Меттью Ревес', 'name': 'Программирование на Python', 'jshanr': 'Программирование', 'str':385},
    ]

    return render_template('example.html',name=name, group=group, curs=curs, lab=lab, fruits=fruits, book=book)

@lab2.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@lab2.route('/lab2/game/')
def game():
    return render_template('lab2game.html' )