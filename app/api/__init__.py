# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restplus import Api
bp = Blueprint('api', __name__)


api = Api(
    bp,
    version='1.0',
    title='disposable email',
    description='disposable email API',
    doc='/',
)

from .views import *
