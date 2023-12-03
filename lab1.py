from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code=302)


@lab1.route("/menu")
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
                <li><a href="/lab2" target="_blank">Лабораторная работа 2</a></li>
                <li><a href="/lab3" target="_blank">Лабораторная работа 3</a></li>
                <li><a href="/lab4" target="_blank">Лабораторная работа 4</a></li>
                <li><a href="/lab5/str" target="_blank">Лабораторная работа 5</a></li>
                <li><a href="/lab6" target="_blank">Лабораторная работа 6</a></li>
                <li><a href="/lab7" target="_blank">Лабораторная работа 7</a></li>

            </ol>
        </main>

        

        <footer>
            &copy: Юстиниан Шишкин, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""

@lab1.route("/lab1")
def lab():
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

@lab1.route('/lab1/oak')
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
@lab1.route('/lab1/student')
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

@lab1.route('/lab1/python')
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

@lab1.route('/lab1/tornado')
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