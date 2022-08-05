from flask_restful import Resource, request
from flask import jsonify
import os
import json

from functions.add_data_func import addDataFunc

class AddData(Resource):
    def post(self):
        jsn = {}
        data = request.data
        data = json.loads(data)

        firstName = data.get('firstName')
        lastName = data.get('lastName')
        age = data.get('age')
        gender = data.get('gender')
        address = data.get('address')

        res = json.dumps(addDataFunc(
                first_name = firstName,
                last_name = lastName,
                a_ge = age,
                g_ender = gender,
                a_ddress = address,
        ))

        res = json.loads(res)
        res = res[0]

        jsn = {"status": res.get('status'), "message": res.get('message'), "body": res.get('body')}

        return jsn
