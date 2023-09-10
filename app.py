from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
    return """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Шишкин Юстиниан Михайлович, лабораторная 1t</title>
</head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        <header>

        <h1>web-сервер на flask<h1>

        <footer>
            &copy: Юстиниан Шишкин, ФБИ-14, 3 курс, 2023
        <footer>
    </body>
</html>
"""

