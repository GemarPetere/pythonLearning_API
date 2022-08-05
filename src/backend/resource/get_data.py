from flask_restful import Resource, request
from flask import jsonify
import json
import os

from functions.get_data_func import getDataFunc

class GetData(Resource):
    def get(self):
        jsn = {}
        data = request.data
        data = json.loads(data)

        id = data.get('user_id')

        res = json.dumps(getDataFunc(id = id))

        res = json.loads(res)
        res = res[0]

        jsn = {"status": res.get('status'), "message": res.get('message'), "body": res.get('body')}
        return jsn


