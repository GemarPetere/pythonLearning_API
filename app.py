from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

from resource.add_data import AddData
from resource.delete_data import DeleteData




app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)




api.add_resource(AddData, '/api/v1/addData')

if __name__ == '__main__':
    app.run(debug=True)