# -*- coding: utf-8 -*-
from .site import bp as site_bp
from .api import bp as api_bp

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings/base.py')

    with app.app_context():
        app.register_blueprint(site_bp)
        app.register_blueprint(api_bp, url_prefix='/api')
    return app


application = app = create_app()
