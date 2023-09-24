from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")

def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>НГТУ, ФБ, Лабораторные работы</title>
    <link rel="stylesheet" type="text/css" href="/static/lab1.css">
</head>
    <body>
        <header>
           НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных работ
        </header>
        <main>
            <ol>
                <li><a href="/lab1" target="_blank">Лабораторная работа 1</a></li>
            </ol>
        </main>

        

        <footer>
            &copy: Юстиниан Шишкин, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return """
    <!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>НГТУ, ФБ, Лабораторная работа 1</title>
    <link rel="stylesheet" type="text/css" href="/static/lab1.css">
</head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная 1
        </header>

        <h1>web-сервер на flask</h1>

        <main>
            <div>
                Flask — фреймворк для создания веб-приложений на языке
                программирования Python, использующий набор инструментов
                Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                называемых микрофреймворков — минималистичных каркасов
                веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
            </div>

             <a href="/menu" target="blank">Меню</a>

            <h2>Реализованные роуты</h2>

            <ul>
                <li><a href="/lab1/oak">/lab1/dub-дуб</a></li>
                <li><a href="/lab1/student">/lab1/student-я</a></li>
                <li><a href="/lab1/python">/lab1/python-python</a></li>
                <li><a href="/lab1/tornado">/lab1/tornado</a></li>
            </ul>
        </main>

        <footer>
            &copy: Юстиниан Шишкин, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""

@app.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<head>
<link rel="stylesheet" type="text/css" href="/static/lab1.css">
</head>
<html>
    <body class = "oak">

    <header>
            
    </header>

    <main>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') +'''" style = "width: 800px; height: 500px;">
    </main>

       
    <footer>
        &copy: Юстиниан Шишкин, ФБИ-14, 3 курс, 2023
    </footer>

    </body>

</html>

'''
@app.route('/lab1/student')
def student():
    return '''
<!doctype html>
<head>
<link rel="stylesheet" type="text/css" href="/static/lab1.css">
</head>
<html>
    <body class = "neti">

    <header>
            
    </header>
    <main style = "text-align: center">
        <h1>Шишкин Юстиниан Михайлович</h1>
         <img src="''' + url_for('static', filename='neti2.jpg') +'''"">
    </main>


    <footer style="color: black" >
         &copy: Юстиниан Шишкин, ФБИ-14, 3 курс, 2023
    </footer>
    </body>

    
</html>

'''

@app.route('/lab1/python')
def python():
    return '''
<!doctype html>
<head>
<link rel="stylesheet" type="text/css" href="/static/lab1.css">
</head>
<html>
    <body class = "python2">

    <header>
    </header>

    <main style = "text-align: center">
         <h1>PYTHON</h1>
            <img class = "python" src="''' + url_for('static', filename='python2.jpg') +'''"">

         <div class = "text">
            Python в русском языке встречаются названия пито́н или па́йтон — высокоуровневый язык программирования общего назначения 
            с динамической строгой типизацией и автоматическим управлением памятью, ориентированный на повышение производительности 
            разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ
         </div>

         <div class = "text">
            Язык является полностью объектно-ориентированным в том плане, что всё является объектами. Необычной особенностью 
            языка является выделение блоков кода пробельными отступами. Синтаксис ядра языка минималистичен, за счёт чего 
            на практике редко возникает необходимость обращаться к документации. Сам же язык известен как интерпретируемый 
            и используется в том числе для написания скриптов. Недостатками языка являются зачастую более низкая скорость работы 
            и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых 
            языках, таких как C или C++.
         </div>

         <div>
            <img class =  src="''' + url_for('static', filename='python.jpg') +'''"">
        </div>
        
    </main>
        
    <footer>
        &copy: Юстиниан Шишкин, ФБИ-14, 3 курс, 2023
    </footer>
    </body>
</html>

'''

@app.route('/lab1/tornado')
def tornado():
    return '''
<!doctype html>
<head>
<link rel="stylesheet"  type="text/css" href="/static/lab1.css">
</head>
<html>
    <body class = "tornado">
        
    </body>
    <header>

    </header>

    <main style = "text-align: center" >
        <h1>Энергетический напиток TORNADO</h1>
        <img class = "tornado2" src="''' + url_for('static', filename='tornado.jpg') +'''"">

        <div class = "text">
            Энергетический напиток Tornado Energy Storm объемом 1 литр - это идеальный выбор для тех, кто хочет получить заряд 
            энергии и бодрости на весь день. Этот напиток содержит кофеин и таурин для повышения энергии и концентрации, 
            а также витамины для поддержания здоровья организма.
            Состав напитка включает подготовленную воду, сахар, лимонную кислоту, ароматизаторы, красители, консерванты и витамины, 
            что делает его уникальным и полезным для здоровья.
        </div>

        <div class = "text" >
            Tornado Energy содержит натуральные ингредиенты, такие как яблоко и имбирь, которые придают напитку неповторимый вкус 
            и аромат. Этот энергетический напиток не содержит консервантов, что делает его еще более безопасным для здоровья.
            Способ применения Tornado Energy прост и удобен: откройте бутылку и налейте напиток в стакан, затем добавьте лед 
            или смешайте с другими напитками для получения еще большего заряда энергии.
            Преимущества Tornado Energy очевидны: этот энергетический напиток поможет вам оставаться бодрым и энергичным 
            в течение всего дня, поддерживая ваш организм витаминами и полезными веществами. Кроме того, этот напиток доступен 
            по доступной цене, что делает его идеальным выбором для всех, кто ценит свое здоровье и энергию.
        </div>

    </main>

     <footer>
            &copy: Юстиниан Шишкин, ФБИ-14, 3 курс, 2023
        </footer>

</html>

'''

@app.route('/lab2/example/')
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

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/game/')
def game():
    return render_template('lab2game.html' )