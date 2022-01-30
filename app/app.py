from flask import Flask
from containers import ApplicationContainer

import views


def create_app():
    container = ApplicationContainer()
    container.config.from_yaml("config.yml")

    app = Flask(__name__)
    app.container = container

    app.add_url_rule("/", "index", views.index)
    app.add_url_rule("/health", "health", views.health)

    return app
