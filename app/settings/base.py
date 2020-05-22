# -*- coding: utf-8 -*-
import os

API_URL = '/api'
API_DOCS_ENABLED = True

# https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY
SECRET_KEY = "test-test-test-test-1234"

# http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/
MONGODB_SETTINGS = {
    'DB': 'disposable_email',
    'host': 'localhost',
    'port': 27017,
}
