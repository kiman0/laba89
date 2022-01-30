from flask import jsonify
from dependency_injector.wiring import inject
from services import Enviroment


@inject
def index():
    return "Hello, World!"


@inject
def health(enviroment: Enviroment):
    return jsonify({"env": enviroment.get_env()})
