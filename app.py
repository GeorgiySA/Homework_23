import os

from flask import Flask, abort, request, jsonify

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query")
def perform_query():
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    cmd1 = request.args.get("cmd1")
    val1 = request.args.get("val1")
    cmd2 = request.args.get("cmd2")
    val2 = request.args.get("val2")
    file_name = request.args.get("file_name")
    if not cmd1 and val1 and file_name:
        abort(400, "Необходимо указать: cmd1, val1 и file_name")
    file_path = os.path.join(DATA_DIR, file_name)
    # проверить, что файл file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    if not os.path.exists(file_path):
        abort(400, "Указанный файл не найден")
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов
    # сконструировать запрос и вернуть пользователю сформированный результат
    return app.response_class('', content_type="text/plain")
