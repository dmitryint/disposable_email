# -*- coding: utf-8 -*-
from .. import api

from flask_restplus import Resource
from flask import Response
import json


@api.route('/login', methods=["GET"])
@api.expect(validate=True)
class Login(Resource):
    @api.response(200, 'OK')
    @api.response(403, 'Forbidden')
    @api.response(400, 'Bad Request')
    def get(self):
        data = {
            "response": "pong"
        }
        return Response(json.dumps(data), mimetype='application/json')
