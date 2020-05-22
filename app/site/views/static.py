# -*- coding: utf-8 -*-
from .. import bp

from flask import render_template, abort
from jinja2 import TemplateNotFound

__all__ = [
    'show'
]


@bp.route('/', defaults={'page': 'index'})
@bp.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
