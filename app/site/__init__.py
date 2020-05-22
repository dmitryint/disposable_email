# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint('site', __name__, template_folder='templates')

from .views import *
