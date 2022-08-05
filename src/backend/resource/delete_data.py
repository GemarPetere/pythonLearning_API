from flask_restful import Resource, request
from flask import jsonify
import os
import json

from functions.delete_data_func import deleteDataFunc

class DeleteData(Resource):
    def delete(self):
        jsn = {}
        data = request.data
        data = json.loads(data)

        id = data.get('user_id')

        res = json.dumps(deleteDataFunc(id = id))

        res = json.loads(res)
        res = res[0]

        jsn = {"status": res.get('status'), "message": res.get('message'), "body": res.get('body')}
        return jsn