from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from pprint import pprint
import Model

app = Flask(__name__)
api = Api(app)

class FlaskrApi(Resource):
    def get(self):
        db = Model.DB()
        energies = db.sq(Model.Energy).all()
        list_entries = [[energy.name] for energy in energies]
        return list_entries
 
    '''
    def post(self):
        data = request.form['data'
        pprint(data)
        return {"a": 1}
    '''
          
api.add_resource(FlaskrApi, '/api')


if __name__ == '__main__':
    app.run(debug=True)