
from flask import Flask
from flask_restful import Resource, Api 

from rotate import RotatePdf

app = Flask(__name__)
api = Api(app)

api.add_resource(RotatePdf, '/submit')

if __name__ == '__main__':
    app.run(debug=True)

