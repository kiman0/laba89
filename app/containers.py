from dependency_injector import containers, providers
from flask import Flask

import views, services


class ApplicationContainer(containers.DeclarativeContainer):

    config = providers.Configuration()

    env = providers.Factory(services.Enviroment, env=config.env)
