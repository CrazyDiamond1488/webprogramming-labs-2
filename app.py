from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return """

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>НГТУ, ФБ, Лабораторные работы</title>
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
        </main>

        <footer>
            &copy: Юстиниан Шишкин, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>

"""

